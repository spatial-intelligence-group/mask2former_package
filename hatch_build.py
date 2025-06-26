# # Builds the MSDeformAttn CUDA kernel
# # - set the CUDA_HOME environment variable before running this script

import os
import glob
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from setuptools import setup
from torch.utils.cpp_extension import (
    BuildExtension,
    CppExtension,
    CUDAExtension,
    CUDA_HOME,
)

import torch


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        print(">> Compiling CUDA extension...")

        root_dir = Path(self.root)

        # The directory structure used for the sdist preparation
        extensions_dir = root_dir / "src" / "MultiScaleDeformableAttention" / "src"
        if not extensions_dir.exists():
            # The directory structure used when building the wheel
            extensions_dir = root_dir / "MultiScaleDeformableAttention" / "src"

        sources = glob.glob(str(extensions_dir / "*.cpp"))
        sources += glob.glob(str(extensions_dir / "cpu" / "*.cpp"))

        extension = CppExtension
        extra_compile_args = {"cxx": []}
        define_macros = []

        if (os.environ.get("FORCE_CUDA") or torch.cuda.is_available()) and CUDA_HOME is not None:
            extension = CUDAExtension
            sources += glob.glob(str(extensions_dir / "cuda" / "*.cu"))
            define_macros += [("WITH_CUDA", None)]
            extra_compile_args["nvcc"] = [
                "-DCUDA_HAS_FP16=1",
                "-D__CUDA_NO_HALF_OPERATORS__",
                "-D__CUDA_NO_HALF_CONVERSIONS__",
                "-D__CUDA_NO_HALF2_OPERATORS__",
            ]
        else:
            raise RuntimeError("CUDA required. Set FORCE_CUDA=1 or ensure torch.cuda.is_available() returns True.")

        ext = extension(
            "MultiScaleDeformableAttention._C",
            sources,
            include_dirs=[str(extensions_dir)],
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
        )

        output_dir = root_dir / "src" / "MultiScaleDeformableAttention"
        output_dir.mkdir(parents=True, exist_ok=True)
        setup(
            name="MultiScaleDeformableAttention",
            ext_modules=[ext],
            cmdclass={"build_ext": BuildExtension},
            script_args=["build_ext", "--build-lib", str(output_dir)],
        )

        print(">> Done building CUDA extension.")