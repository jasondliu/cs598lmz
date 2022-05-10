import ctypes
ctypes.cast(None, ctypes.py_object)

import os
import sys

try:
    import numpy as np
except ImportError:
    np = None

try:
    from . import mpi4py_fft
    from .mpi4py_fft import fft, ifft
except ImportError:
    mpi4py_fft = None

try:
    from . import mpi4py_fftx
    from .mpi4py_fftx import fft, ifft
except ImportError:
    mpi4py_fftx = None

try:
    from mpi4py import MPI
except ImportError:
    MPI = None

# Set path to the directory containing this file.
# This should allow us to run the tests from any subdirectory.
dirname = os.path.dirname
if len(dirname(dirname(dirname(dirname(dirname(dirname(dirname(dirname(__file__))))))))):
    os.chdir(dirname(dirname(dirname(dirname(dirname(dirname
