import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def pwr(a,b):
    return a**b

def lshift(a,b):
    return a << b

def rshift(a,b):
    return a >> b

def and_(a,b):
    return a & b

def or_(a,b):
    return a | b

def xor(a,b):
    return a ^ b

def not_(a):
    return ~a

def neg(a):
    return -a

def cmp(a,b):
    return a < b

def cmp_eq(a,b):
    return a == b

def cmp_neq(a,b):

