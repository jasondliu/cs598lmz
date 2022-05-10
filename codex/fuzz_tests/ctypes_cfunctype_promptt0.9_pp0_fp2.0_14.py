import ctypes
# Test ctypes.CFUNCTYPE for unbounded function pointer types.
from ctypes import *
values = [
    c_int(1234), c_double(1.2345), c_float(1.2345), c_char('a'),
    c_wchar('a'), c_long(0xffff), c_ulong(0xffffffff),
    c_byte(0xff), c_ubyte(0xff),
    pointer(c_long(0xffff)), pointer(c_char('a')),
    pointer(c_wchar('a'))]

# types.FunctionType(code, globals, name, argdefs, closure)
if '__pypy__' in sys.builtin_module_names:

    def f1():
        pass

    def f2(a):
        return a

    def f3(a, b):
        return a, b

    def f4(a, b, c):
        return a, b, c

    def f5(a, b, c, d):
        return a, b, c, d

    def f6
