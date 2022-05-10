import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
import sys
import time
import traceback
import types

import numpy

import pyopencl as cl
import pyopencl.array
import pyopencl.clrandom
import pyopencl.characterize
import pyopencl.clmath
import pyopencl.clrandom
import pyopencl.tools

import pytest

import logging
logger = logging.getLogger("test_cl")

try:
    import pyopencl.clmath_ext
except ImportError:
    pass

try:
    import pyopencl.clrandom_ext
except ImportError:
    pass

try:
    import pyopencl.clblas
except ImportError:
    pass

try:
    import pyopencl.clsparse
except ImportError:
    pass

try:
    import pyopencl.clblas_ext
except ImportError:
    pass

try:
    import pyopencl.clsparse_ext
except ImportError:
    pass

