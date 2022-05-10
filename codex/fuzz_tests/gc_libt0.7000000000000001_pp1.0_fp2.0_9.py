import gc, weakref, os
from functools import partial
import numpy as np

from . import stats
from . import io
from . import metrics
from . import pd
from . import utils


class Dataset(object):
    """
    Abstract class for datasets

    """
    def __init__(self, path=None):
        """
        Initialize dataset

        Parameters
        ----------
        path : str
            path to dataset
        """
        self._path = path

    def open(self, path=None):
        """
        Open dataset

        Parameters
        ----------
        path : str
            path to dataset
        """
        if path is not None:
            self._path = path
        if self._path is None:
            raise ValueError('Path must be specified to open dataset')
        self._open()

    def close(self):
        """
        Close dataset
        """
        self._close()

    def read(self, indices, roi=None, channel_indices=None, **kwargs):
        """
        Read data from dataset

        Parameters

