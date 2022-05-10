import gc, weakref
import copy

import numpy as np

import pyopencl as cl
from pyopencl import array
from pyopencl.reduction import ReductionKernel

import pycuda.driver as cuda
from pycuda.compiler import SourceModule
from pycuda.gpuarray import GPUArray

from gpaw.mpi import world, rank
from gpaw.utilities import unpack
from gpaw.utilities.blas import axpy
from gpaw.utilities.timing import Timer
from gpaw.utilities.memory import maxrss
from gpaw.utilities.tools import tri2full
from gpaw.utilities.lapack import general_diagonalize
from gpaw.utilities.gauss import gauss
from gpaw.utilities.blacs import BlacsGrid
from gpaw.utilities.blacs import BlacsDescriptor
from gpaw.utilities.blacs import Redistributor
from gpaw.utilities.blacs import block_cyclic
from gpaw.utilities.blacs import block_cyclic_redistribute
from gpaw
