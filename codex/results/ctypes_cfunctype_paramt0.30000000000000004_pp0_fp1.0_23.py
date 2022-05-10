import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def my_function(x):
    return x**2

my_function_c = FUNTYPE(my_function)

def my_function_2(x):
    return x**3

my_function_c_2 = FUNTYPE(my_function_2)

def my_function_3(x):
    return x**4

my_function_c_3 = FUNTYPE(my_function_3)

def my_function_4(x):
    return x**5

my_function_c_4 = FUNTYPE(my_function_4)

def my_function_5(x):
    return x**6

my_function_c_5 = FUNTYPE(my_function_5)

def my_function_6(x):
    return x**7

my_function_c_6 = FUNTYPE(my_function_6)

def my_function_7(x):
    return x**8

my_function_c_7 = FUNTYPE(my
