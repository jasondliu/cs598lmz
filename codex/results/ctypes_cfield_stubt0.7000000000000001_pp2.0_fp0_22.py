import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'C(%r)' % (self.value,)
    def _get(self, obj):
        return C(self.value + obj.value)
    def _set(self, obj, value):
        obj.value = self.value - value.value
    c_f = ctypes.CField(None, _get, _set)

S._fields_.append(('c_f', C(1)))

print S().c_f
print S().c_f = C(2)
print S().c_f
