import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

for name in ['_fields_', '_field_defaults_', '_Fields', '_field_dict',
             '__doc__', '__dict__', '_bases_', '_file_', '_name_',
             '_flags_', '_abstract_', '_is_structclass_', '_is_unionclass_',
             '_byteswapped_']:
    ctypes.Structure.__dict__[name] = ctypes.CField.__dict__[name]

class _Pointer(ctypes._Pointer):

    def __call__(self, value=None):
        if value is None:
            return self
        restype = self._type_
        if not isinstance(value, (restype, ctypes._SimpleCData)):
            raise TypeError("expected %r, got %r" % (restype, value))
        return value

    __getitem__ = __call__

ctypes._Pointer = _Pointer

def setattr_ctypes(self, key, value):
    try:
