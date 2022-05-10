import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.c_int)
# function : x, y, z, r, rho, tx_in, nx, ny
fun = FUNTYPE(lambda x, y, z, r, rho, tx_in, nx=1, ny=1, nz=1: ny)
# function : x, y, z, r, rho, tx_in, nx, ny
C_F_define = NP_A.from_pyfunc(fun, 5, 1)
#C_F_define = NP_A.from_pyfunc(fun, 5, 0)
C_map.F_define = C_F_define


#C_F_define = NP_A.from_pyfunc(lambda x, y, z, r, rho: 0, 5, 1)


