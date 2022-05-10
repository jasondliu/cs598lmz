import ctypes
# Test ctypes.CFUNCTYPE_CDECL
result = ctypes.CFUNCTYPE_CDECL(None, None)
print result

# Test ctypes.CFUNCTYPE_FASTCALL
result = ctypes.CFUNCTYPE_FASTCALL(None, None)
print result

# Test ctypes.CFUNCTYPE_PASCAL
result = ctypes.CFUNCTYPE_PASCAL(None, None)
print result

# Test ctypes.CFUNCTYPE_STDCALL
result = ctypes.CFUNCTYPE_STDCALL(None, None)
print result

# Test ctypes.CFUNCTYPE_MSVC
result = ctypes.CFUNCTYPE_MSVC(None, None)
print result
