import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunction(object):
    def __init__(self, ptr, argtypes, restype):
        self.ptr = ptr
        self.argtypes = argtypes
        self.restype = restype
    def __call__(self, *args):
        res = self.ptr(*args)
        if self.restype is not None and self.restype is not ctypes.py_object:
            res = self.restype(res)
        return res

class CStructType(object):
    def __init__(self, name, fields, opaque=False):
        self.name = name
        self.opaque = opaque
        self.fields = fields
        self.ctype = type(name, (ctypes.Structure,), {})
        if not opaque:
            for (fieldname, fieldtype) in fields:
                setattr(self.ctype, fieldname, ctypes.CField(fieldtype))
    def __repr__(self):
        return "<CStructType %s>" % (self.name,)

class CField(object):
