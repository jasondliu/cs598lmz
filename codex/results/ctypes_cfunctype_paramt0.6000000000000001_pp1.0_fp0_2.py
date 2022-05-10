import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def add1(x):
    return x+1

def add2(x,y):
    return x+y

def add3(x,y,z):
    return x+y+z

def add4(x,y,z,t):
    return x+y+z+t

def add5(x,y,z,t,u):
    return x+y+z+t+u

def add6(x,y,z,t,u,v):
    return x+y+z+t+u+v

add1_cfunc = FUNTYPE(add1)
add2_cfunc = FUNTYPE(add2)
add3_cfunc = FUNTYPE(add3)
add4_cfunc = FUNTYPE(add4)
add5_cfunc = FUNTYPE(add5)
add6_cfunc = FUNTYPE(add6)

add1_cfunc2 = FUNTYPE(add1)
add2_cfunc2 = FUNTYPE(add2
