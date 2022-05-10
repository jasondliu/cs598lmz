import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bug report from Konstantin Baydarov <kbaidarov@gmail.com>
# See http://bugs.python.org/issue14196
#

import sys
import ctypes
from ctypes import *

def test_cfunc_ret(ret, cfunc, *args):
    cfunc.restype = ret
    x = cfunc(*args)
    print(x, type(x))
    cfunc.restype = None

def test_cfunc_arg(arg, cfunc, *args):
    cfunc.argtypes = [arg]
    x = cfunc(*args)
    print(x, type(x))
    cfunc.argtypes = []

def test_cfunc_both(ret, arg, cfunc, *args):
    cfunc.argtypes = [arg]
    cfunc.restype = ret
    x = cfunc(*args)
    print(x, type(x))
    cfunc.restype = None
    cfunc.argtypes = []

