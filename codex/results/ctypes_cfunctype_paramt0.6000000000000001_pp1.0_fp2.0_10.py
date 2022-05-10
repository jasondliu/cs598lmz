import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
def c_sf_bessel_I1(x):
    return math.sin(x)/x**2
c_sf_bessel_I1_c = FUNTYPE(c_sf_bessel_I1)
c_sf_bessel_I1_c_ptr = ctypes.cast(c_sf_bessel_I1_c, ctypes.POINTER(ctypes.c_double))

c_sf_bessel_J1 = FUNTYPE(sf.bessel_J1)
c_sf_bessel_J1_ptr = ctypes.cast(c_sf_bessel_J1, ctypes.POINTER(ctypes.c_double))

c_sf_bessel_Y1 = FUNTYPE(sf.bessel_Y1)
c_sf_bessel_Y1_ptr = ctypes.cast(c_sf_bessel_Y1, ctypes.POINTER(ctypes.c_double))

x_min=-5
x
