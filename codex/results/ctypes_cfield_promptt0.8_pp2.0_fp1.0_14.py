import ctypes
# Test ctypes.CField with a non-type argument.
try:
    ctypes.CField(1)
except TypeError:
    print('TypeError')
except:
    print('Non-TypeError exception thrown')

# Test ctypes.CField with a non-ctypes data type.
try:
    ctypes.CFiel
