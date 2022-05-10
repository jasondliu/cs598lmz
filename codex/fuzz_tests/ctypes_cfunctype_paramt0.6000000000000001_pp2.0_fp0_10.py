import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
CFUNC = FUNTYPE(cfunc)

# Plot the result
x = np.linspace(0, 10, 1000)
y = [CFUNC(x0) for x0 in x]

plt.plot(x, y)
plt.show()
</code>

