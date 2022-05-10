import ctypes
# Test ctypes.CField
lib.cfield_foo.restype = ctypes.CField(ctypes.c_int)
# Test ctypes.CField.__get__
lib.cfield_foo.restype.__get__(None, None)
# Test ctypes.CField.__set__
lib.cfield_foo.restype.__set__(None, None)

# Test ctypes.CFuncPtr
lib.cfuncptr_foo.restype = ctypes.CFuncPtr(ctypes.c_int)
# Test ctypes.CFuncPtr.__get__
lib.cfuncptr_foo.restype.__get__(None, None)
# Test ctypes.CFuncPtr.__set__
lib.cfuncptr_foo.restype.__set__(None, None)

# Test ctypes.CDLL
ctypes.CDLL("")
# Test ctypes.CDLL.__getattr__
ctypes.CDLL("").__getattr__("")
# Test ctypes.CDLL.__getitem__
ctypes.CDLL("").__getitem
