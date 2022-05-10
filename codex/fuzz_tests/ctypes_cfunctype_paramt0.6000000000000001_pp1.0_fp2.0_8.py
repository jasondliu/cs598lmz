import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double)

def myf(x, y, z):
    return x**2 + y**2 + z**2

f = FUNTYPE(myf)

print f(1, 2, 3)

# 1.
print '1.'
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# 2.
print '2.'
x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y)
plt.show()

# 3.
print '3.'
x = np.linspace(-10, 10, 100)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, 'r', x, z, 'b')
plt.show()

# 4.
