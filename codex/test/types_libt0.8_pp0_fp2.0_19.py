import types
types.FunctionType = types.MethodType

# prevent accidental loading of incompatible ctypes.so
# for more information, see https://github.com/numpy/numpy/issues/1456
import ctypes
ctypes.PyDLL = None

# prevent accidental loading of incompatible ctypes.so from libgcc_s
# for more information, see https://github.com/numpy/numpy/issues/1456
import ctypes.util
ctypes.util.find_library = lambda lib: ''

# we need to define the following symbols before importing modules from distutils
import imp
import numpy
_dummy = imp.find_module("numpy")
del imp, numpy

from distutils.ccompiler import new_compiler
from Cython.Distutils import build_ext
from h5py.highlevel import File
import h5py
import sys
import os

def get_cython_extensions():
    import numpy
    
    ret = []
    
