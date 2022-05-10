import mmap
import numpy as np
import mindspore.dataset as ds
import mindspore.dataset.vision.c_transforms as vision
import mindspore.dataset.transforms.c_transforms as c_vision
import mindspore.dataset.transforms.py_transforms
import mindspore.dataset.vision.py_transforms as py_vision
import mindspore.dataset.vision.ndarray as mnd
import mindspore.dataset.transforms.c_transforms as cds
from mindspore._c_dataengine import _ExecutionContext
from mindspore.common import dtype as mstype
from mindspore.dataset.vision.c_transforms import RandomCropWithBBox, RandomHorizontalFlipWithBBox

DATA_DIR = ["../data/dataset/test_tf_file_3_images/train-0000-of-0001.data"]
SCHEMA_DIR = "../data/dataset/test_tf_file_3_images/datasetSche
