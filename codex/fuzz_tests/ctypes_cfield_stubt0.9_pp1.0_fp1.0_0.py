import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(PropertyType):
    def annotate(self, name, owner, **kwds):
        self.name = name
        self.owner = owner
        self.fldtype = kwds['type']

    def specialize(self, env):
        self.mytype = env[self.fldtype]

    def read(self, f):
        return f.read_type(self.mytype)

    def write(self, f, v):
        f.write_type(self.mytype, v)

    def c_repr(self):
        return "ctypes.c_%s" % self.mytype.ctype

CLIB_TYPES['struct-field'] = CField

class CStruct(ContainerType):
    ctype = 'struct'
    c_repr_fmt = "ctypes.Structure"
    def __init__(self, name, size = None, align = None, packed = None,
                 parent = None, child = None, child_key = None, fields = None,
                 prefix = None,
