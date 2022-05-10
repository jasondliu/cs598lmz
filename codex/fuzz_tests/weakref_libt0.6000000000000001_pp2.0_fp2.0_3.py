import weakref

import numpy as np

import pyopencl as cl

from pyopencl.tools import dtype_to_ctype

import pyopencl.array as clarray

import pyopencl.clrandom as clrand

import pyopencl.cltypes as cltypes

import pyopencl.scan as clscan

import pyopencl.clmath as clmath

import pyopencl.elementwise as cle

import pyopencl.algorithm as clalgo

from pyopencl.characterize import has_double_support

import logging

import sys

# {{{ debugging

def _debug_memory_usage ():

from pyopencl.tools import get_glob_mem_size

from pyopencl.characterize import get_host_memory_usage

from pyopencl.tools import MemoryUsage

from pyopencl.compyte.dtypes import get_or_register_dtype

from collections import defaultdict

mem_size = get_glob_mem_size()

avail_mem_size = get_host_
