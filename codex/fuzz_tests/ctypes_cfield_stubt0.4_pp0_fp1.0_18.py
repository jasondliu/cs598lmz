import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def g(x):
    return x

def f(x):
    return g(x)

def test(x):
    return f(x)

test(S(1))

# ____________________________________________________________

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def g(x):
    return x

def f(x):
    return g(x)

def test(x):
    return f(x)

test(S(1))

# ____________________________________________________________

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def g(x):
    return x

def f(x):
    return g(x)

def test(x):
    return f(x)

test(S(1))

# ____________________________________________________________

class S(ctypes.St
