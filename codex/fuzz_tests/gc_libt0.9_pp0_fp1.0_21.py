import gc, weakref
import numpy as np

from circus.shared.messages import print_and_log
from circus.shared.mpi import is_root, get_shared_comm, get_max_processes


class SharedArray(object):
    """
    virtual base class for shared arrays
    """
    def __init__(self, shape, dtype, **kwargs):
        self._shape = shape
        self._dtype = dtype
        self._nbytes = self._shape[0] * self._shape[1] * np.dtype(self._dtype).itemsize

    def __repr__(self):
        return '<SharedArray shape=%s, dtype=%s, maxsize=%d>' % (self._shape, self._dtype, self.get_max_size())

    def __str__(self):
        return '<SharedArray shape=%s, dtype=%s, maxsize=%d>' % (self._shape, self._dtype, self.get_max_size())

    def as_numpy(self):

