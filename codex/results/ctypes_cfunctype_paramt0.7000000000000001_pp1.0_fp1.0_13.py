import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

def _export(func):
  if not isinstance(func, FUNTYPE):
    func = FUNTYPE(func)
  func_name = func.__name__
  if hasattr(sys, 'setdlopenflags'):
    old_flags = sys.getdlopenflags()
    sys.setdlopenflags(old_flags | ctypes.RTLD_GLOBAL)
    func.restype = ctypes.py_object
    ctypes.CDLL(lib_path, mode=ctypes.RTLD_GLOBAL).__setattr__(func_name, func)
    sys.setdlopenflags(old_flags)
  else:
    func.restype = ctypes.py_object
    ctypes.CDLL(lib_path, mode=ctypes.RTLD_GLOBAL).__setattr__(func_name, func)
  return func

@_export
def Coefficient(x, y, z):
  return np.array([x, y, z])

@_export
def Input(key,
