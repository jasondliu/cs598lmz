import gc, weakref
from threading import Thread
from multiprocessing import Process
from functools import partial
from queue import Empty as EmptyException
from time import time
from collections import OrderedDict, Sequence

from numpy import ndarray, asarray, arange, zeros, ones, empty, uint8, uint16,\
    int16, float32, float64, complex64, complex128, dtype, frombuffer, \
    fromstring, fromiter, fromfile, memmap, array, vstack, hstack, amax, amin, \
    ndim, column_stack, row_stack, isscalar, dtype, \
    result_type, float_, intc, int_, longlong, intp, uintc, uint, ulonglong, \
    uintp, double, float_, longfloat, cfloat, clongfloat, float16, float32, \
    float64, float96, float128, float256, \
    complex_, complex64, complex128, complex192, complex256, \
    number, bool_, integer, inexact, floating, complexflo
