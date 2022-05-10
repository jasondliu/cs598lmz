import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

def func(x):
    return x**2-a

a = 10
interval = np.linspace(-10, 10, 100)
y = func(interval)
plt.plot(interval, y)
plt.show()


gsl = ctypes.cdll.LoadLibrary('libgsl.so')
gsl.gsl_interp_accel_alloc.argtypes = [ctypes.c_int]
gsl.gsl_interp_accel_init.restype = ctypes.c_void_p
gsl.gsl_interp_accel_init.argtypes = [ctypes.c_int]
gsl.gsl_interp_alloc.argtypes = [ctypes.c_void_p, ctypes.c_int]
gsl.gsl_interp_init.restype = ctypes.c_void_p
gsl.gsl_interp_init.argtypes = [ctypes.c_void_p, ctypes.
