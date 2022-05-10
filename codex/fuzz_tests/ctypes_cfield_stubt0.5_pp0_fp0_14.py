import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self._objects = []

    def __getattr__(self, name):
        if name.startswith('_'):
            return super(C, self).__getattr__(name)

        for obj in self._objects:
            if name in obj._fields_:
                return obj.__getattribute__(name)

        raise AttributeError

class D(C):
    def __init__(self):
        super(D, self).__init__()

        self.__dict__['_objects'] += [S()]

d = D()

print(d.x)
d.x = 5
print(d.x)
</code>
You can use <code>__getattr__</code> to access the fields of the <code>ctypes</code> objects, but you need to make sure that you don't access the fields of the <code>ctypes.Structure</code> objects until they have been initialised, otherwise you'll get an access violation.

