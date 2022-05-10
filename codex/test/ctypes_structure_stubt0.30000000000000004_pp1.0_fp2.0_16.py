import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def foo(a, b):
    return a + b

def bar(a, b):
    return a - b

def baz(a, b):
    return a * b

def qux(a, b):
    return a / b

def quux(a, b):
    return a % b

def corge(a, b):
    return a & b

def grault(a, b):
    return a | b

def garply(a, b):
    return a ^ b

def waldo(a, b):
    return a << b

def fred(a, b):
    return a >> b

def plugh(a, b):
    return -a

def xyzzy(a, b):
    return ~a

def thud(a, b):
    return +a

def r(a, b):
    return a == b

