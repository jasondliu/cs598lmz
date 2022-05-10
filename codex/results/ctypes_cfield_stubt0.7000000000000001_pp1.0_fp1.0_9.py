import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyCField(ctypes.CField):
    def __get__(self, obj, cls):
        return 'spam'
    def __set__(self, obj, value):
        pass

class MyStructure(ctypes.Structure):
    _fields_ = [('x', MyCField)]

s = MyStructure()
print s.x
s.x = 'ham'
