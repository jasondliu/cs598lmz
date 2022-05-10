import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))

def callback(id, x, v):
  return x[0]


try:
  lib = ctypes.CDLL("../lib/liball_states.so")
except OSError as e:
  lib = ctypes.CDLL("../cmake-build-release/liball_states.so")
  
num_vars = 2
var_bounds = (ctypes.c_double * (num_vars * 2))()
for i in range(num_vars):
  var_bounds[i] = -10.0
  var_bounds[num_vars + i] = 10.0

#tolerance = 1e-14
tolerance = 1e-8

lib.init(FUNTYPE(callback), num_vars, ctypes.c_double(tolerance), var_bounds, 1)
lib.run()
num_dirs = lib.
