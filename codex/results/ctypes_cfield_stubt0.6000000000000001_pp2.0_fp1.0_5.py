import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# this is a function that will be called from Python
def add(a, b):
    return a + b

# this is a function that will be called from Python
def sub(a, b):
    return a - b

# this is a function that will be called from Python
def mul(a, b):
    return a * b

# this is a function that will be called from Python
def div(a, b):
    return a / b

# this is a function that will be called from Python
def mod(a, b):
    return a % b

# this is a function that will be called from Python
def pow(a, b):
    return a ** b

# this is a function that will be called from Python
def lshift(a, b):
    return a << b

# this is a function that will be called from Python
def rshift(a, b):
    return a >> b

# this is a function that will be called from Python
def get_x(a):
    return a.x

# this is a function that will be
