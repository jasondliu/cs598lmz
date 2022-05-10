import ctypes
# Test ctypes.CFUNCTYPE
try:
    ctypes.CFUNCTYPE
except AttributeError:
    print("SKIP")
    raise SystemExit

def f_1(x):
    return x

def f_2(x, y):
    return x + y

def f_3(x, y, z):
    return x + y + z

def f_4(x, y, z, t):
    return x + y + z + t

def f_5(x, y, z, t, u):
    return x + y + z + t + u

def f_6(x, y, z, t, u, v):
    return x + y + z + t + u + v

def f_7(x, y, z, t, u, v, w):
    return x + y + z + t + u + v + w

def f_8(x, y, z, t, u, v, w, q):
    return x + y + z + t + u + v + w + q

