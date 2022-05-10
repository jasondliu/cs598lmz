import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
def repr_field(self):
    return '<Field type=%s, offset=%d>' % (self._type_, self.offset)
ctypes.CField.__repr__ = repr_field

class X(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('x', X), ('y', Y)]

# This should display the type, offset and size of each field
# in the structure, union or class.
def dump(obj):
    print '%s: %s' % (obj.__name__, obj._fields_)
    for name, typ in obj._fields_:
        print '  %s' % repr(getattr(obj, name))

dump(S)
print
dump(X)
print
dump(Y)
print
dump(Z)
