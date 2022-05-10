import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))
def func(x):
    return x[0]**2 + x[1]**2
func_ = FUNTYPE(func)

x = np.array([1.0, 1.0])
xopt = ctypes.c_double(0.0)

xopt = ctypes.c_double(0.0)

# using the native python interface:
res = fmin_l_bfgs_b(func, x, approx_grad=True)
print(res)

# using the ctypes interface:
res = fmin_l_bfgs_b(func_, x, approx_grad=True)
print(res)
</code>

