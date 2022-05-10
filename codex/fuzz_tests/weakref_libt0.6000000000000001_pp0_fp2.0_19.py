import weakref

import numpy as np

from . import _compat
from . import cuda_array
from . import cuda_stream
from . import cuda_context
from . import cuda_memory

from .cuda_compiler import CUDACompiler

from . import cuda_convnet
from . import cuda_kernel

#from . import cuda_convnet
#from . import cuda_kernel

class CUDARuntimeError(RuntimeError):
    pass

class CUDAContext(object):
    def __init__(self, device_id=0, use_lock=True):
        self.context = cuda_context.CUDAContext(device_id, use_lock)
        self.memmap = weakref.WeakValueDictionary()
        self.compiler = CUDACompiler()
        self.compiler.precompile(self.context)

    def __enter__(self):
        self.context.__enter__()
        return self

    def __exit__(self, type, value, traceback):
