import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

func = FUNTYPE(f)
print(func(2))

#=========================

#make instance of type
x = ctypes.c_double(3.0)

#make instance of type
y = ctypes.c_double(4.0)

#call function
print(func(x))

#call function
print(func(y))
