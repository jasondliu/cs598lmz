import mmap, os
import pickle

import numpy as np

from ..utils import _ensure_tuple, _get_cache_dir
from ._utils import _get_mnist_data, _get_svhn_data


class DataSet:
    def __init__(self, X, y, shuffle=False, random_state=None):
        self._X = X
        self._y = y
        self._shuffle = shuffle
        self._random_state = random_state
        self._num_examples = X.shape[0]
        self._epochs_completed = 0
        self._index_in_epoch = 0

    @property
    def X(self):
        return self._X

    @property
    def y(self):
        return self._y

    @property
    def num_examples(self):
        return self._num_examples

    @property
    def epochs_completed(self):
        return self._epochs_completed

