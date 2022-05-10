import ctypes
# Test ctypes.CFUNCTYPE, keyword args
from ctypes import *

try:
    WINFUNCTYPE
except NameError:
    WINFUNCTYPE = CFUNCTYPE

from ctypes import _testcall as t

# keyword args
# XXX this is not supported in IronPython yet
if not is_cli:
    prototype = WINFUNCTYPE(c_int, paramflags=1)
    params = (1,), dict(paramflags=1)
    assert prototype(*params) == 1

# prototype(None) should return a function prototype
prototype = WINFUNCTYPE(c_int, c_int, c_int)
functype = prototype(None)

assert isinstance(functype, WINFUNCTYPE)
# prototype has a func_closure, functype has not
assert functype.func_closure is None
assert prototype.func_closure is not None

# now call the prototype
res = prototype(c_int, c_int)(1, 2)
assert res == 3

class X(Structure):
    _fields_ = [("a",
