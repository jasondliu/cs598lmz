import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, np.ndpointer(dtype=np.double), np.ctypeslib.ndpointer(dtype=np.double), np.ctypeslib.ndpointer(dtype=np.double),  ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)

sumx= open('sumx.txt', 'w')
sumy= open('sumy.txt', 'w')
sumz= open('sumz.txt', 'w')
sumxx= open('sumxx.txt', 'w')
sumxy= open('sumxy.txt', 'w')
sumxz= open('sumxz.txt', 'w')
sumyy= open('sumyy.txt', 'w')
sumyz= open('sumyz.txt',
