import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.CField):

    def __init__(self, *args, **kwargs):
        self._default = None
        ctypes.CField.__init__(self, *args, **kwargs)

    def get_data(self, instance):
        if self._default is None:
            self._default = self._type()
        return instance._data.setdefault(self._name, self._default)

class D(S):
    _fields_ = S._fields_ + [('x', C(ctypes.c_int))]

def main():
    d = D()
    print d.x
    d.x = 1
    print d.x
    d.x = 2
    print d.x

if __name__ == '__main__':
    main()
