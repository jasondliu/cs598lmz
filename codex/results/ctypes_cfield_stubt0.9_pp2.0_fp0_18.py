import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, *args, **kw):
        self.test = kw.pop('test', False)
        super(CField, self).__init__(*args, **kw)

for tp in [str, unicode]:
    del tp.__dict__['__format__']
    assert tp.__format__ == object.__format__

assert str.__new__(str, '123').__format__('x') == 'x'
assert u'123'.__format__('x') == 'x'

class S(ctypes.Structure):
    _fields_ = [(name, CField)]

assert getattr(ctypes.CDLL(ctypes.util.find_library('c'), use_errno=False), '_fgets').argtypes == [ctypes.POINTER(ctypes.c_char), ctypes.c_int, ctypes.c_void_p]
assert getattr(ctypes.CDLL(ctypes.util.find_library('c'), use
