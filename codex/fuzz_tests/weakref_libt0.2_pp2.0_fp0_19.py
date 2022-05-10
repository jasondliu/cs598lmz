import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_enum_type, new_struct_type, new_union_type,
    new_pointer_type, new_array_type, new_function_type, new_raw_pointer_type,
    new_void_type, new_primitive_type, new_opaque_type,
    new_constant_string, new_constant_wide_string,
    new_global_var, new_global_constant,
    new_global_constant_int, new_global_constant_long, new_global_constant_longlong,
    new_global_constant_float, new_global_constant_double,
    new_global_constant_longdouble,
    new_global_constant_char, new_global_constant_wchar,
    new_global_constant_char16, new_global_constant_char32,
    new_global_constant_uchar, new_global_constant_ush
