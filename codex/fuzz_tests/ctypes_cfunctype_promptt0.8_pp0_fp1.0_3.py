import ctypes
# Test ctypes.CFUNCTYPE if that works, otherwise use ctypes.WINFUNCTYPE
try:
  CFUNCTYPE = ctypes.CFUNCTYPE
except AttributeError:
  CFUNCTYPE = ctypes.WINFUNCTYPE

# Test if safe functions are available, in case they are not use _safe_ functions
if hasattr(ctypes, 'c_ssize_t'):
  c_ssize_t = ctypes.c_ssize_t
else:
  c_ssize_t = ctypes.c_int

def CMPFUNC(name):
  return CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

def PFUNC(name):
  return CFUNCTYPE(c_ssize_t, ctypes.c_void_p, ctypes.c_void_p)

def IPFUNC(name):
  return CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)


