import ctypes
# Test ctypes.CField.from_address
import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

for i in range(10):
    x = X.from_address(lib._testfunc_i_p(i))
    print(x.a)

# Ensure that the result is not a subclass
assert type(X.from_address(lib._testfunc_i_p(1))) is type(X())

# Issue #14251: memory leak
import gc
for i in range(1024):
    lib._testfunc_i_p(i)
gc.collect()
for i in range(1024):
    lib._testfunc_i_p(i)
gc.collect()

# Check that we can pass None as a template
print(ctypes.Structure.from_address(lib._testfunc_i_p(1), None))
