import gc, weakref, types
from . import _cffi_backend

class _new_primitive_type(object):
    def __init__(self, name, ctypeobj, c_name, c_type, c_size, c_align,
                 is_primitive_integer, is_primitive_float,
                 is_primitive_char, extra_repr=''):
        self.name = name
        self.ctypeobj = ctypeobj
        self.c_name = c_name
        self.c_type = c_type
        self.c_size = c_size
        self.c_align = c_align
        self.is_primitive_integer = is_primitive_integer
        self.is_primitive_float = is_primitive_float
        self.is_primitive_char = is_primitive_char
        self.extra_repr = extra_repr
        self._incomplete_error = None

    def __repr__(self):
        return '<ctype %s%s at %x>' % (self.
