import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

def test():
    c = C(1, 2, 3)
    c.x = c.y = c.z = 42
    if c.x != 42 or c.y != 42 or c.z != 42:
        raise RuntimeError("wrong field assignment")
    for name in 'xyz':
        if c.__dict__[name] != 42:
            raise RuntimeError("wrong field assignment")
    for name in 'zyx':
        if getattr(c, name) != 42:
            raise RuntimeError("wrong field assignment")
    C.x = ctypes.c_int(42)
    if c.x != 42 or c.y != 42 or c.z != 42:
        raise RuntimeError("wrong field assignment")
    C.x = ctypes.c_int(42)
    if c.x != 42 or c.y != 42
