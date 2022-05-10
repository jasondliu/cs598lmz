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

