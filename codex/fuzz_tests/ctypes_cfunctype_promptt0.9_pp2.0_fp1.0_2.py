import ctypes
# Test ctypes.CFUNCTYPE and ctypes.c_float in the presence of a Python
# subtype of c_float.

import ctypes
from ctypes import *

class Sub_float(c_float):
    pass

print Sub_float

a = Sub_float(2.2)
print a
print type(a)
print a.value

PythonAPI = cdll.python27
print PythonAPI
print PythonAPI._testfunc_p_f

@CFUNCTYPE(c_int, c_float)
def testfunc(a):
    print "testfunc:", type(a), a
    print "   type:", type(a.value)
    
print testfunc
r = testfunc(a)

print r
print type(r)
