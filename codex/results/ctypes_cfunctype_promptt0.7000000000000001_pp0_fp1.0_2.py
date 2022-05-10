import ctypes
# Test ctypes.CFUNCTYPE with calling convention
from ctypes import *
from _ctypes_test import func, func_si, func_p_p, func_p_i, func_p_d

print 'Calling convention "cdecl" ...'
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)
cmp = CMPFUNC(func)

print cmp(1, 2)
print cmp(3, 4)
print cmp(5, 6)
print

CMPFUNC = CFUNCTYPE(c_int, c_char_p, c_char_p)
cmp = CMPFUNC(func_p_p)
print cmp("Hello", "world")
print cmp("Hello", "Hello")
print cmp("world", "Hello")
print

CMPFUNC = CFUNCTYPE(c_int, c_double, c_double)
cmp = CMPFUNC(func_p_d)
print cmp(1.0, 2.0)
print cmp(3.0, 4.0
