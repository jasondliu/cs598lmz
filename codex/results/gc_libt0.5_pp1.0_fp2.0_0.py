import gc, weakref
from contextlib import contextmanager
import numpy as np
import numba

from . import _cuda
from . import _cuda_api
from . import _cudadrv
from . import _driver
from . import _dtypes
from . import _utils
from . import _autoinit

_debug = False

def _debug_print(*args):
    if _debug:
        print(*args)

class CUDAMemoryError(MemoryError):
    """CUDA memory allocation failed.

    The CUDA driver reported that it was unable to satisfy the
    allocation request.  This error is unrecoverable and will
    be raised regardless of the error handling preferences.
    """

class CUDAMemoryManager(object):
    """
    Manage CUDA memory allocations.

    There is one instance of this class per CUDA context, stored
    in the `_cudadrv._context._memory_manager` attribute.
    """

    def __init__(self):
        self.allocs = {}
        self.active_allocs = {}
        self.active_
