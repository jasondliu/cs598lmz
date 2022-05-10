import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def F(x):
    # return 1.0
    return x*x-2.0
def dF(x):
    # return 0.0
    return 2.0*x
    
def secant(x,y,F,eps,maxiter):
    xprev = x
    x = y
    for i in range(0,maxiter):
        print "iteration %d: x=%f" % (i,x)
        f = F(x)
        fprev = F(xprev)
        d = (x-xprev)/(f-fprev)
        xnext = x - d*f
        if (abs(xnext-x) < eps):
            return xnext
        xprev = x
        x = xnext
    raise ValueError("secant method did not converge")
    
f = FUNTYPE(F)
df = FUNTYPE(dF)
x0 = 2.0
eps = 1e-10
maxiter = 100
print "secant method:"
x1 = secant(
