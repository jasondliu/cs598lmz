import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

class Y(ctypes.c_int):
    def __repr__(self):
        return '<Y>'

class Z(int):
    pass

for typ in (X, Y, Z):
    print(typ)
    print(type(typ._type_))
    print(type(typ._type_).__bases__)
    print(type(typ._type_).__base__)
    print(type(typ._type_).__base__.__base__)
    print(type(typ._type_).__base__.__base__.__base__)

print(type(ctypes.c_int))
print(type(ctypes.c_int).__bases__)
print(type(ctypes.c_int).__base__)
print(type(ctypes.c_int).__base__.__base__)

print(type(ctypes.c_int(1)))
print(type(ctypes.c_int(1)).__bases
