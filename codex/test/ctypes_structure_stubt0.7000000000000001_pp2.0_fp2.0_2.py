import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short

def pack_struct(x, y):
    s = S()
    s.x = x
    s.y = y
    return s

def unpack_struct(s):
    return (s.x, s.y)

assert unpack_struct(pack_struct(0, -1)) == (0, -1)

# ____________________________________________________________

class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_long)]

def f():
    s = S()
    return s.a

assert f() == 0

# ____________________________________________________________

class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_long)]

def f():
    s = S()
    s.a = -1
    return s.a

assert f() == -1

# ____________________________________________________________

