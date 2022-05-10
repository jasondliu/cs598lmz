import weakref

import numpy as np

from . import _base
from .. import util


class _Uniform(_base.Uniform):
    def __init__(self, *args, **kwargs):
        self._ref = weakref.ref(self)
        super().__init__(*args, **kwargs)

    def _init_data(self):
        self._data = np.zeros(self.shape, dtype=self.dtype)

    def _get_data(self):
        return self._data

    def _set_data(self, data):
        self._data = data


class _Texture2D(_base.Texture2D):
    def __init__(self, *args, **kwargs):
        self._ref = weakref.ref(self)
        super().__init__(*args, **kwargs)

    @property
    def _data(self):
        return self._ref()._data

    @_data.setter
    def _data(self, data):
        self._ref()._data = data

    def _init_data
