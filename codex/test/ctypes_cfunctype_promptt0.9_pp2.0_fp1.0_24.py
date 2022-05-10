import ctypes
# Test ctypes.CFUNCTYPE and argtypes-kwargtypes syntax
# This is a pretty general test for defining callbacks
# into the interpreter.  The argtypes-kwargtypes syntax
# does not mean it should be used for all.
import _ctypes_test

try:
    callproc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
        _ctypes_test.callproc)
except AttributeError:
    pass
else:
    try:
        assert callproc(1, 1) == 2
        assert callproc(1) == 1
        assert callproc(1, k=999) == 1000
        assert callproc(1, k=999) == 1000
        assert callproc(k=999, a=1) == 1000
    except TypeError:
        raise AssertionError("argtypes-kwargtypes syntax failed")

print('TEST COMPLETE')
