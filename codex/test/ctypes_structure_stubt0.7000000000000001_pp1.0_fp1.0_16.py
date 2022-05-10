import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_double
    z = ctypes.c_char*7

def get_struct():
    # x = S(x=12, y=1.23, z='foo')
    x = S()
    x.x = 12
    x.y = 1.23
    x.z = 'foo'
    return x

