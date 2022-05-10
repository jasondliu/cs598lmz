import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def unmarshal(f):
    if hasattr(f, '_obj'):
        return f._obj
    else:
        return f

def marshal(f):
    if hasattr(f, '_type_'):
        return f
    else:
        return f._type_()

def field_offset(field):
    return field.offset

def field_size(field):
    return field.size

def field_type(field):
    return field._type_

def field_set(field, obj, value):
    field_pointer(field, obj)[0] = value

def field_get(field, obj):
    return field_pointer(field, obj)[0]

def field_address(field, obj):
    return obj + field.offset

def field_pointer(field, obj):
    return ctypes.cast(obj + field.offset,
                       ctypes.POINTER(field._type_))

def structure_size(structure):
    return ctypes.sizeof(structure)

def structure_
