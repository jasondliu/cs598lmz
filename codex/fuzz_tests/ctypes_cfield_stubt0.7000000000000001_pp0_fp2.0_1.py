import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(S):
    pass

print(type(S2.x))
print(isinstance(S2.x, ctypes.CField))

class C:
    def __init__(self):
        self.x = 1

C.x = 2

print(C().x)

class MyStruct(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
               ]

m = MyStruct()

m.y = 2
print(m.y)

m.myfield = 3
# m.myfield = 3.1

print(m.myfield)

class MyUnion(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_char),
                ('z', ctypes.c_int),
               ]

u = MyUnion()

u.y = b'a'

print(
