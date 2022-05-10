import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def test(name, restype, argtypes):
    func = CFUNCTYPE(restype, *argtypes)
    print func, func.__name__

test("foo", c_int, [])
test("bar", c_int, [c_int])
test("baz", c_int, [c_int, c_int])

test("foo", c_int, [c_int, c_int])
test("foo", c_int, [c_int, c_int, c_int])
test("foo", c_int, [c_int, c_int, c_int, c_int])
test("foo", c_int, [c_int, c_int, c_int, c_int, c_int])

test("foo", c_int, [c_int] * 10)
test("foo", c_int, [c_int] * 20)
test("foo", c_int, [c_int] * 100)

test("foo", c_int, [c_int
