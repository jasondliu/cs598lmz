import ctypes
# Test ctypes.CFUNCTYPE
import_module('_testcapi')
from _testcapi import func_with_varargs, func_with_varargs_caller
from _testcapi import func_accepts_varargs, PyCFuncPtr
from _testcapi import func_with_keywords, func_with_keywords_caller
from _testcapi import func_accepts_keywords, PyCKeyFuncPtr

PYFUNCTYPE = ctypes.CFUNCTYPE

f = func_with_varargs()
assert isinstance(f, PYFUNCTYPE)
assert f(1, 2, 3, 4, 5) == 15

f = func_with_varargs_caller()
assert isinstance(f, PYFUNCTYPE)
assert f(1, 2, 3, 4, 5) == 15

f = func_accepts_varargs()
assert isinstance(f, PYFUNCTYPE)
assert f(1, 2, 3, 4, 5) == 15

f = PyCFuncPtr(1, 2, 3)
