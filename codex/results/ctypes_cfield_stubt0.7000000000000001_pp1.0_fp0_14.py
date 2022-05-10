import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def charp_to_str(charp):
    return ctypes.cast(charp, ctypes.c_char_p).value.decode('ascii')

def get_field_type(field):
    return type(ctypes.cast(field.offset, ctypes.c_void_p).value)

def get_field_offset(field):
    return ctypes.cast(field.offset, ctypes.c_void_p).value

def get_field_size(field):
    return ctypes.sizeof(get_field_type(field))

def get_pointer_size():
    return ctypes.sizeof(ctypes.c_void_p)

def get_ptr(addr, type):
    return ctypes.cast(ctypes.c_void_p(addr), type)

def get_ptr_type(ptr):
    return type(ptr)._type_

def get_ptr_size(ptr):
    return ctypes.sizeof(get_ptr_type(ptr))

def get_ptr_value
