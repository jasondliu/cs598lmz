import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    v = ctypes.c_void_p

x = S()
print(x.v)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char),
                ('v', ctypes.c_void_p)]

x = S()
print(x.v)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char),
                ('v', ctypes.c_void_p)]
    def __init__(self):
        print('__init__')
        self.x = b'A'
        self.v = self

    def __del__(self):
        print('__del__')

x = S()
print(x.v)
y = x.v
print(y.v)
