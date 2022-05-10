import ctypes
# Test ctypes.CField() with a non-existent field
try:
    ctypes.CField()
except TypeError:
    pass
else:
    print('CField() without arguments should raise TypeError')
