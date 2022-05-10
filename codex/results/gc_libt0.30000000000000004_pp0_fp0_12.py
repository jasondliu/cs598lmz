import gc, weakref, sys, os
import numpy as np
import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule
import pycuda.gpuarray as gpuarray
from pycuda.tools import dtype_to_ctype
import pycuda.cumath
import pycuda.elementwise as elementwise
from pycuda.elementwise import ElementwiseKernel
import pycuda.reduction as reduction
import pycuda.scan as scan
from pycuda.scan import ExclusiveScanKernel

from pycuda.tools import context_dependent_memoize
from pycuda.tools import dtype_to_ctype
from pycuda.tools import DeviceData

from pycuda.compiler import SourceModule

from pycuda.gpuarray import GPUArray
from pycuda.gpuarray import _get_common_dtype
from pycuda.gpuarray import _get_dtype_num
from pycuda.gpuarray import _get_struct_fmt
from pycuda.gpuarray import _get_struct
