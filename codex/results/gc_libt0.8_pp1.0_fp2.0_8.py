import gc, weakref

import numpy as np

from .base import BaseDataset, _check_list_of_dicts
from .utils import (
    _collate_bbox, _collate_class_label, _collate_img, _collate_mask,
    _collate_proposal, _collate_prop_labels, _collate_filename,
    _collate_vector
)

def _get_dataset_info(dataset_name, info):
    """Get the dataset information.

    Examples
    --------
    >>> # info = mxnet.gluon.utils.load_json('./info.json')
    >>> dataset_name = 'coco'
    >>> info = _get_dataset_info(dataset_name, info)
    >>> root = info.pop('root')
    >>> cls_dataset = gluoncv.data.COCODetection
    >>> train_dataset = cls_dataset(root=root, splits=('instances_train2017',), **info)


