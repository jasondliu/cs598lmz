import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2
f_c = FUNTYPE(f)

def f2(x):
    return np.sin(x)
f2_c = FUNTYPE(f2)

def f3(x):
    return x**3
f3_c = FUNTYPE(f3)

x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

X,Y = np.meshgrid(x,y)
Z = np.zeros_like(X)
for i in range(100):
    for j in range(100):
        Z[i,j] = f_c(X[i,j])

plt.figure()
plt.pcolor(X,Y,Z)
plt.colorbar()
plt.contour(X,Y,Z,20)
plt.show()

Z2 = np.zeros_like(X)
for i in range(100):
