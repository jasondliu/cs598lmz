import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double,ctypes.c_double)

def f(a,b):
    return a+b

f_c = FUNTYPE(f)

print(f_c(1.0,2.0))

#Here is a more complicated example:

# C Declarations
# typedef double (*FUNTYPE)(double,int,double*);
# double f(double,int,double*);

# Python
# import ctypes
# FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.POINTER(ctypes.c_double))
# def f(a,n,arr):
#    return a+sum(arr)
# f_c = FUNTYPE(f)
# arr = (ctypes.c_double*3)(3.0,4.0,5.0)
# print(f_c(1.0,3,arr))

#Here is a more complicated example:

# C Declarations

