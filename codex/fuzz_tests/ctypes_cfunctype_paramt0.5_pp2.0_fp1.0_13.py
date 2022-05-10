import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Uncomment this for the C version
#import ctypes
#lib = ctypes.CDLL("./libcos.so")
#lib.cos.restype = ctypes.c_double
#lib.cos.argtypes = (ctypes.c_double,)
#fastcos = lib.cos

# Uncomment this for the Fortran version
fastcos = FORTRAN_MODULE.fastcos

# Uncomment this for the Fortran version
#fastcos = ctypes.CDLL("./libfastcos.so").fastcos
#fastcos.restype = ctypes.c_double
#fastcos.argtypes = (ctypes.c_double,)

# Uncomment this for the Cython version
#import pyximport
#pyximport.install()
#import fastcos_cython
#fastcos = fastcos_cython.fastcos

# Uncomment this for the Numba version
#import numba
#fastcos = numba.jit(nopython=True)(math.
