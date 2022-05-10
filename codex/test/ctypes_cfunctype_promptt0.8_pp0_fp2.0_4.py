import ctypes
# Test ctypes.CFUNCTYPE(None)
try:
    TestError
except NameError:
    TestError = AssertionError

try:
    ctypes.CFUNCTYPE(None)
except AttributeError:
    may_raise(AttributeError)
