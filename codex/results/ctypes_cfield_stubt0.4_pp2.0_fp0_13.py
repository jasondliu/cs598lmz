import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__get__ = lambda self, obj, cls: obj.__dict__[self.__name__]
ctypes.CField.__set__ = lambda self, obj, value: setattr(obj, self.__name__, value)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s = S()
s.x = 1
print(s.x)

s.x = 2
print(s.x)
</code>
Output:
<code>1
2
</code>

