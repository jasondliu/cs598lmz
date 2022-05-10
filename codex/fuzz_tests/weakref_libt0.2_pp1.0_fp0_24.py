import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_enum_type, new_struct_type, new_union_type,
    new_pointer_type, new_array_type, new_function_type,
    new_global_var, new_raw_api, new_primitive_type,
    new_void_type, new_constant_string,
    new_constant_int, new_constant_long, new_constant_float,
    new_constant_double, new_constant_longdouble,
    new_constant_char, new_constant_wchar,
    new_constant_int_signed, new_constant_int_unsigned,
    new_constant_long_signed, new_constant_long_unsigned,
    new_constant_longlong_signed, new_constant_longlong_unsigned,
    new_constant_ssize_t, new_constant_size_t,
    new_constant_intptr_t,
