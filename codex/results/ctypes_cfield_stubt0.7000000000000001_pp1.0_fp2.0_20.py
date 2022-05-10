import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField:
    def fget(self):
        print("fget")
        return self._value

    def fset(self, value):
        print("fset")
        self._value = value

    def __get__(self, obj, type=None):
        print("__get__", obj, type)
        if obj is None:
            return self

        return self.fget(obj)

    def __set__(self, obj, value):
        print("__set__", obj, value)
        self.fset(obj, value)


class F(ctypes.Structure):
    _fields_ = [('x', CField())]

f = F()
f.x = 2
print(f.x)
</code>

