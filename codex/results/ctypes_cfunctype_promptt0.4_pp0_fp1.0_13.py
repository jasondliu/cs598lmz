import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def check(res, func, args):
    print func.__name__, repr(args), "->",
    try:
        print repr(res)
    except:
        print "EXCEPTION"

def test(tp):
    print
    print "testing", tp.__name__
    f = CFUNCTYPE(tp)
    check(f(lambda: None), f, ())
    check(f(lambda x: None), f, (c_int,))
    check(f(lambda x, y: None), f, (c_int, c_int))
    check(f(lambda x, y, z: None), f, (c_int, c_int, c_int))

for tp in [c_int, c_float, c_double, c_char_p, c_void_p]:
    test(tp)

for tp in [c_int, c_float, c_double, c_char_p, c_void_p]:
    test(POINTER(tp))

