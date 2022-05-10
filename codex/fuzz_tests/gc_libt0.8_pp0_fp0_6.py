import gc, weakref

import numpy as np

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
from pycuda.compiler import SourceModule
from pycuda.scan import ExclusiveScanKernel
import skcuda.linalg

try:
    from skcuda.linalg import _get_linalg_error_if_any
except ImportError:
    # some versions of skcuda do not have this function;
    # in that case, use a no-op function
    def _get_linalg_error_if_any(status):
        pass

from . import blas_kernel_source
from . import random_kernel_source
from . import simplify
from . import stypes

from .linalg import linalg_options

from .memory import Memory
from .tools import (context, alloc_like, gpu_sync, get_el_gpu, get_el_host,
                    ensure_dtype, ensure_args_are_arrays, ensure_args_are_gpuarray,
                    ensure_gpu_cont
