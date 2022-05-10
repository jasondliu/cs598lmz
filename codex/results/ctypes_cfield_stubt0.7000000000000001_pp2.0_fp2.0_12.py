import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, attr):
        return self.__dict__[attr]

class CField(C):
    def __repr__(self):
        return str(self.__dict__)

# This is not correct, but good enough for now.
print('import ctypes.wintypes')

for name in dir(ctypes.wintypes):
    if name.startswith('LP_'):
        continue
    if name.startswith('_'):
        continue
    real = getattr(ctypes.wintypes, name)
    if type(real) is type(ctypes.c_int):
        print('ctypes.wintypes.%s = CField(%r)' % (name, real))
    else:
        print('ctypes.wintypes.%s = %r' % (name, real))

print()
print('import ctypes
