import ctypes
# Test ctypes.CField
try:
    ctypes.CField("foo")
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Test ctypes.Field
try:
    ctypes.Field("foo")
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Test ctypes.PyCFuncPtr
try:
    ctypes.PyCFuncPtr("foo")
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Test ctypes.CFuncPtr
try:
    ctypes.CFuncPtr("foo")
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Test ctypes.CData
try:
    ctypes.CData("foo")
except TypeError:
    pass
else:
    print("should have raised TypeError")
