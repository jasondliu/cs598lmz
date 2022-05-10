import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
%timeit fun()

CYTHONFUNTYPE = cpdef(FUNTYPE)
@CYTHONFUNTYPE
def cythonfun():
    return None
%timeit cythonfun()

def fun2():
    return None
CYTHONFUNTYPE = cpdef(FUNTYPE)
@CYTHONFUNTYPE
def cythonfun2():
    return None
%timeit cythonfun2()

CYTHONFUNTYPE = cpdef(FUNTYPE)
@CYTHONFUNTYPE
def cythonfun3():
    return None
%timeit cythonfun3()

def fun3():
    return None
%timeit fun3()

%timeit cythonfun()
%timeit cythonfun2()
%timeit cythonfun3()
 
%timeit fun()
%timeit fun2()
%timeit fun3()
 
import math
%timeit math.exp(1)
 
def myexp(x):
    return math.exp(x)
%
