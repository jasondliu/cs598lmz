import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_void_p,
                          ctypes.c_void_p)
f = FUNTYPE(2.0)

def f(x1,x2,y1,y2,s1,s2,sigma1,sigma2,rho1,rho2,q,z1,z2):
    return tf.exp(-0.5*((x1-y1)**2/(s1**2)+tf.pow(x2-y2,2)/(s2**2)-2*rho1*(x1-y1)*(x2-y2)/(s
