import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)


class CField(object):
    def __init__(self, name, ptype, iid, packed=False):
        assert isinstance(ptype, ctypes._SimpleCData)
        self.name = name
        self.ptype = ptype
        self.iid = iid
        self.packed = packed

    def __repr__(self):
        return 'CField(%r, %r, %r, %r)' % (self.name, self.ptype, self.iid, self.packed)

class CArray(ctypes.Array):
    def __new__(cls, ptype, *args):
        assert isinstance(ptype, ctypes._SimpleCData)
        return ctypes.Array.__new__(cls, ptype, *args)

class CUnion(ctypes.Union):
    _fields_ = None
    _anonymous_ = None
    _pack_ = None
    def __new__(cls, pname, pfields, p_pack_=None, _pack_=None, _anonymous
