import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

pt = POINT(10, 20)
# In fact, the ctypes.c_int is an instance of ctypes.CField
assert isinstance(pt.x, ctypes.CField)
assert pt.x.offset == 0
assert pt.y.offset == 4

# Test ctypes.CDLL
cdll = ctypes.CDLL
# Test ctypes.DLLHandle
dll = cdll(None)
assert isinstance(dll, ctypes.DLLHandle)

print(dll.GetCurrentThreadId.argtypes)
dll.GetCurrentThreadId.argtypes = [ctypes.c_int, ctypes.c_int]
print(dll.GetCurrentThreadId.argtypes)

# Test ctypes.CDLLLoadError
try:
    cdll.LoadLibrary('')
except ctypes.CDLLLoadError as e:
    assert e.name == ''

# Test ctypes.
