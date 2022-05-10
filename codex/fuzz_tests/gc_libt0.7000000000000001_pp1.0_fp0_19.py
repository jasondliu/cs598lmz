import gc, weakref
from warnings import warn
import operator
from collections import deque
from functools import wraps
from itertools import islice
import copy
import numpy as np

try:
    from pycuda.driver import Context, Device, Event, MemoryPool
except ImportError:
    from . import cuda_compat as cuda
    from .cuda_compat import Context, Device, Event, MemoryPool
import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.cumath as cumath

from . import cublas, cusolver
from . import cusparse as cusparse
from . import curandom as curandom
from . import cudnn as cudnn
from . import util

from . import rng_mrg
from . import rng_philox
from . import rng_sobol
from . import rng_xor
from . import rng_mtgp32

import pycuda.tools

from pycuda.tools import dtype_to_ctype
import pycuda.driver as
