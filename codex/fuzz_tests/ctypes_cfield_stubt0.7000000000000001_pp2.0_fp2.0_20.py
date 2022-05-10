import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def _is_CField(typ):
    return type(typ) is ctypes.CField

def _is_CStruct(typ):
    return issubclass(typ, ctypes.Structure)

@register(b'\x03')
def _(typ, value):
    if isinstance(typ, ctypes.CField):
        return typ.from_buffer(value)
    elif _is_CStruct(typ):
        return typ.from_buffer_copy(value)
    else:
        return bytes(value)

@register(b'\x04')
def _(typ, value):
    if isinstance(typ, ctypes.CField):
        return typ.from_buffer(value)
    elif _is_CStruct(typ):
        return typ.from_buffer_copy(value)
    else:
        return bytes(value)

@register(b'\x05')
def _(typ, value):
    return int.from_bytes(value, 'little')

@register(b'\x06')

