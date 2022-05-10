import ctypes
# Test ctypes.CField.
class X(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.CField, None),
        ('c', ctypes.c_int),
        ]
# Check that it is not possible to create instances of CField.
try:
    x = ctypes.CField()
except TypeError:
    pass
else:
    raise RuntimeError, "CField instances should not be constructible"
# Check that it is not possible to create instances of the class that
# contains a CField.
try:
    x = X()
except TypeError:
    pass
else:
    raise RuntimeError, "X instances should not be constructible"
# Check that it is not possible to create instances of subclasses of
# the class that contains a CField.
class Y(X):
    pass
try:
    x = Y()
except TypeError:
    pass
else:
    raise RuntimeError, "Y instances should not be constructible"
