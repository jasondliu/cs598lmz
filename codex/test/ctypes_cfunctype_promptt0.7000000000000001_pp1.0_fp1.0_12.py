import ctypes
# Test ctypes.CFUNCTYPE() with a simple function
# Returns:
#   0 on success
#   1 on error
def test_CFUNCTYPE1(dll):
  f = ctypes.CFUNCTYPE(ctypes.c_int)(('test_CFUNCTYPE1', dll))
  if f() != 0:
    return 1

  return 0

def test_CFUNCTYPE2(dll):
  # Test ctypes.CFUNCTYPE() with a function that takes an integer argument
  f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(('test_CFUNCTYPE2', dll))
  if f(0) != 0:
    return 1

  return 0

def test_CFUNCTYPE3(dll):
  # Test ctypes.CFUNCTYPE() with a function that takes an double argument
  f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)(('test_CFUNCTYPE3', dll))
