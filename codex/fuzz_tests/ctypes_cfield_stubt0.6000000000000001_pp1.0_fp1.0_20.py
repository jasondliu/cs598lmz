import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyInt(ctypes.c_int):
    def __new__(cls, value=0):
        return super(MyInt, cls).__new__(cls, value)

class MyField(ctypes.CField):
    _type_ = MyInt

class T(ctypes.Structure):
    _fields_ = [('x', MyField)]

print(type(T.x))
print(type(T().x))
</code>

