import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))

def pythag(a,b):
    absa = abs(a)
    absb = abs(b)
    if (absa > absb):
        return absa*sqrt(1.0+pow(absb/absa,2))
    elif (absb != 0.0):
        return absb*sqrt(1.0+pow(absa/absb,2))
    else:
        return 0.0

def dsvdcmp(a,m,n,w,v):
    itmax=50
    eps=pow(2.0,-52.0)
    tiny=1.0e-20
    flag=0
    nm=n
    if (m<n):
        nm=m
    else:
        nm=n
    rv1 = (ctypes.c_double * n)()
    for i in range(n):
        rv1
