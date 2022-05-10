import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPtr = type(S._fields_[0])  # this is a pointer to PyCFieldObject

# Declarations. This doesn't check if the type of the fields in the
# declaration matches the original structure definition!

def make_struct_declaration(name, fields):
    """Create a new structure declaration as a subclass of 'type'."""
    
    # Fields: [('name', 'type'), ...]
    if isinstance(fields, dict):
        field_names, fields = zip(*fields.items())
    else:
        field_names = [name for name, _ in fields]
    
    def init_simple(self, *args, **kwds):
        for kwd, arg in kwds.items():
            setattr(self, kwd, arg)
        for i, arg in enumerate(args):
            setattr(self, field_names[i], arg)
        return self
    
    # This is the actual class. Inherits from Structure.
    class_attrs = { '_fields_' : fields,
                    '__
