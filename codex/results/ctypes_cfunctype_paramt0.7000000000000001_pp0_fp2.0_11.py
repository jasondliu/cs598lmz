import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_int, ctypes.c_int )

# Callback function
@FUNTYPE
def myfun(a, b):
    print('callback called with:', a, b)
    return a + b

# Callback function
@FUNTYPE
def myfun2(a, b):
    print('callback called with:', a, b)
    return a - b

# Callback function
@FUNTYPE
def myfun3(a, b):
    print('callback called with:', a, b)
    return a * b

# Callback function
@FUNTYPE
def myfun4(a, b):
    print('callback called with:', a, b)
    return a // b

# Callback function
@FUNTYPE
def myfun5(a, b):
    print('callback called with:', a, b)
    return a ** b

# Callback function
@FUNTYPE
def myfun6(a, b):
    print('callback called with:', a, b)
    return a % b

