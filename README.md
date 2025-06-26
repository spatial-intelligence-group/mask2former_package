# Mask2Former: Masked-attention Mask Transformer for Universal Image Segmentation (CVPR 2022)

This is a packaged version of the Mask2Former repository limited to segmentation on images. Check the original repository for more details: https://github.com/facebookresearch/Mask2Former. The repository contains two installable packages:
- `mask2former`: The main Mask2Former package.
- `MultiScaleDeformableAttention`: Multi-scale deformable attention used in Mask2Former.


## Installation

Both packages can be installed via pip directly from the repository:

```bash
pip install git+https://github.com/spatial-intelligence-group/mask2former_package.git
```

Note that [`detectron2`](https://github.com/facebookresearch/detectron2/tree/main/) used by Mask2Former requires PyTorch to be installed at build time, but does not specify so. Therefore, you have to install PyTorch before installing Mask2Former.

If your installation of CUDA toolkit is not in `/usr/local/cuda`, you have to set the environment variable `CUDA_HOME`.


## Basic Usage

You can check the [easy_anon mask generation script](https://github.com/spatial-intelligence-group/easy_anon/src/easy_anon/mask.py) for the basic usage of the Mask2Former package.


## Model Zoo and Baselines

The project provides a large set of baseline results and trained models available for download in the [Mask2Former Model Zoo](https://github.com/facebookresearch/Mask2Former/blob/main/MODEL_ZOO.md).


## License

Shield: [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The majority of Mask2Former is licensed under a [MIT License](LICENSE).

However portions of the project are available under separate license terms: Swin-Transformer-Semantic-Segmentation is licensed under the [MIT license](https://github.com/SwinTransformer/Swin-Transformer-Semantic-Segmentation/blob/main/LICENSE), Deformable-DETR is licensed under the [Apache-2.0 License](https://github.com/fundamentalvision/Deformable-DETR/blob/main/LICENSE).


## <a name="CitingMask2Former"></a>Citing Mask2Former

If you use Mask2Former in your research or wish to refer to the baseline results published in the [Model Zoo](MODEL_ZOO.md), please use the following BibTeX entry.

```BibTeX
@inproceedings{cheng2021mask2former,
  title={Masked-attention Mask Transformer for Universal Image Segmentation},
  author={Bowen Cheng and Ishan Misra and Alexander G. Schwing and Alexander Kirillov and Rohit Girdhar},
  journal={CVPR},
  year={2022}
}
```

If you find the code useful, please also consider the following BibTeX entry.

```BibTeX
@inproceedings{cheng2021maskformer,
  title={Per-Pixel Classification is Not All You Need for Semantic Segmentation},
  author={Bowen Cheng and Alexander G. Schwing and Alexander Kirillov},
  journal={NeurIPS},
  year={2021}
}
```


## Acknowledgement

Code is largely based on MaskFormer (https://github.com/facebookresearch/MaskFormer).
