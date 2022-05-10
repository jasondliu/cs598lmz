import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def f(x):
    return x**2

def g(x):
    return x**3

xv = np.linspace(-2,2,num=50)
yv = [f(x) for x in xv]

xv2 = np.linspace(-1,1,num=50)
yv2 = [g(x) for x in xv]

plt.plot(xv,yv)
plt.plot(xv2,yv2)
plt.xlim(-2,2)
plt.ylim(0,4)


functs = [f,g]

rootf = root(functs[0], x0=1)
rootg = root(functs[1], x0=1)

xu = np.linspace(-2,2,num=100)
pointf = [functs[0](x) for x in xu]
pointg = [functs[1](x) for x
