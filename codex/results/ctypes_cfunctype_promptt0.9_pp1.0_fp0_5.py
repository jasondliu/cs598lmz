import ctypes
# Test ctypes.CFUNCTYPE(*extra_args)(callable)
# for docstring, where *extra_args adds up to 2 values, like
# int and c_char_p uppon the callable's arguments, in the 'argtypes' attribute.
#
# Written by Ingmar Stieger (PAP018)
#
# $Id: test_CFUNCTYPE2.py 58869 2009-12-01 12:10:22Z benjamin.peterson $
#
# Sample code: 

import _ctypes_test
lib = _ctypes_test.load_library('c_test')

def test():
    i = _ctypes_test.c_int(0)
    p = _ctypes_test.c_char_p(b"Hello, world")
    callable = lib.get_int(p)
    assert p.value == b"Hello, world"
    func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, _ctypes_test.c_int)(callable)

    res = func(
