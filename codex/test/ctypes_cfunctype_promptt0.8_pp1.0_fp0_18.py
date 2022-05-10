import ctypes
# Test ctypes.CFUNCTYPE(None)
try:
  dll.TestFunctionPointerWithVoidReturnType.argtypes = (ctypes.CFUNCTYPE(None),)
except:
  print('exception')
else:
  # Test calling TestFunctionPointerWithVoidReturnType
  try:
    dll.TestFunctionPointerWithVoidReturnType(None)
  except:
    print('exception')
  else:
    print('success')

# Test ctypes.CFUNCTYPE(ctypes.c_int)
try:
  dll.TestFunctionPointerWithIntReturnType.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int),)
except:
  print('exception')
else:
  # Test calling TestFunctionPointerWithIntReturnType
  try:
    dll.TestFunctionPointerWithIntReturnType(lambda: 0)
  except:
    print('exception')
  else:
    print('success')

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes
