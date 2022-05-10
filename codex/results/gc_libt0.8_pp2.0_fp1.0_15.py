import gc, weakref
import multiprocessing

import numpy as np

from . import channel
from . import utils

class DataStore(object):
    """
    A DataStore object encapsulates access to the data stored in a h5py file.
    The DataStore object keeps track of the DataChannels that have been accessed
    from it, and when they are deleted, it closes the numpy arrays for these
    channels.

    Parameters
    ----------
    f : h5py.File
        The filename of the h5py file.
    """
    def __init__(self, f):
        self.f = f
        self.groups = {}
        self.channels = weakref.WeakKeyDictionary()
        try:
            self._lock = multiprocessing.Lock()
        except ImportError:
            self._lock = False

        self.set_lock = lambda x: None

    def __getitem__(self, key):
        # locking the file is not necessary when we're only reading data,
        # but it's good for documentation
        self.lock()
        if self
