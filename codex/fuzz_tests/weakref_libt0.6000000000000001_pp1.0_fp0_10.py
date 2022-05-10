import weakref

import numpy as np

from . import _librootnumpy
from .extern.six import string_types


__all__ = [
    'array',
    'tree2array',
    'tree2rec',
    'array2tree',
    'list_branches',
    'list_structures',
    'list_trees',
    'fill_hist',
]


def _check_unsupported_features(tree):
    unsupported_features = []
    if tree.GetCurrentFile().IsZombie():
        unsupported_features.append('TTree::GetCurrentFile().IsZombie()')
    return unsupported_features


def _check_unsupported_array_types(array):
    unsupported_array_types = []
    if array.dtype.fields is not None:
        unsupported_array_types.append(
            'structured arrays with fields of type bool, int, float, or '
            'complex')
    if array.dtype.names is not None:
        for name in array.dtype.names:
            if array[name].
