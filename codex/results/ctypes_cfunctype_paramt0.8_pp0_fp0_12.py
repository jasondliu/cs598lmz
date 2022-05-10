import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def function(x):
    return math.exp(-x*x/2)

cfunc = FUNTYPE(function)

# Adaptive quadrature with singularities
res, err = quad.fixed_quad(cfunc, -1, 1, n=10, points=[0, 1])
print("Fixed quadrature: ", res, err)
res, err = quad.quad(cfunc, -1, 1, weight='alg', wvar=1)
print("Adaptive quadrature: ", res, err)
