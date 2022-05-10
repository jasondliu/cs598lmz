import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class c_void_p(ctypes.c_void_p):
    def __repr__(self):
        if not self:
            return 'None'
        return repr(self.value)

class c_int_p(ctypes.POINTER(ctypes.c_int)):
    def __init__(self, value):
        if isinstance(value, int):
            value = ctypes.c_int(value)
        super(c_int_p, self).__init__(value)

    def __repr__(self):
        return '<c_int_p at %s: %s>' % (self._get_obj(), repr(self.contents))

    def __str__(self):
        return repr(self)

def c_int_p_p(value):
    return ctypes.POINTER(ctypes.POINTER(ctypes.c_int))(value)

class c_char_p(ctypes.c_char_p):
    def __repr__(self):
        if not self:
