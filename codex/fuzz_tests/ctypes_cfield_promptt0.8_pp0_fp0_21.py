import ctypes
# Test ctypes.CField instead of ctypes.Field
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def f(x):
    p = POINT()
    p.x = x
    return p.x

def g(x):
    p = POINT()
    p.x = x
    return p.y

def main():
    for i in xrange(5):
        f(i)
        g(i)

main()
""")

# ____________________________________________________________
#
# assert in a nested function

test_import("nested_assert", """
def f(n):
    if n == 0:
        return n
    f(n-1)

def main():
    f(10)

main()
""")

# ____________________________________________________________
#
# __import__ used as a function

from pypy.rlib.rarithmetic import r_uint, r_longlong
from pypy.rpython.lltypesystem
