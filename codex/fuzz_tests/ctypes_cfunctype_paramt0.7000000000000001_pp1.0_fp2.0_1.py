import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(t, y, yp, ypp, yppp):
    return ypp

f_ = FUNTYPE(f)

#initial conditions
t0 = 0.0
y0 = 0.0
yp0 = 0.0
ypp0 = 1.0
yppp0 = 0.0

tout = np.linspace(t0, 10.0, 100)
yout = []

#call the integrator
for t in tout:
    yout.append(rk78_step(t, y0, yp0, ypp0, yppp0, f_))
    y0, yp0, ypp0, yppp0 = yout[-1]

yout = np.array(yout)

plt.plot(tout, yout[:,0], label='y')
plt.plot(tout, yout[:,1], label='yp
