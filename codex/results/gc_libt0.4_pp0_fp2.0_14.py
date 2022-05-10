import gc, weakref
import sys
import time
import threading
import traceback

import numpy as np

from . import _cudamat as cm
from . import _cudamat_conv as cn
from . import _cudamat_kernels as ck
from . import _cudamat_random as cr
from . import _cudamat_ctc as ct
from . import _cudamat_ctc_kernels as ctc_kernels

from . import cudamat_utils as utils
from . import cudamat_ext as ext

from . import cudamat_conv as conv

from . import cudamat_ctc as ctc

from . import cudamat_random as random

import pycuda.driver as drv

import pycuda.gpuarray as gpuarray

#
# Global variables
#

# Global CUDA context.
global_cublas_handle = None
global_cusolver_handle = None
global_cudnn_handle = None
global_stream = None

