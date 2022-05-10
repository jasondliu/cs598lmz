import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x, y):
    return x**2 + y**2

f_c = FUNTYPE(f)

def f_py(x, y):
    return f_c(x, y)

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

x, y = np.meshgrid(x, y)

z = f_py(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm)
plt.show()
</code>


A:

The problem here is that <code>np.vectorize</code> is not a true vectorization function, but rather a convenience function that wraps the function and calls it with scalar arguments.  In this case, the function that is wrapped is <code>f_c</code>, which is
