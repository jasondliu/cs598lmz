import weakref

from . import _cffi_backend as backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_handle, new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type, new_function_type,
    new_function_type_with_var_arg, new_void_type, new_opaque_type,
    new_enum_type_custom, new_type_from_c_type,
    new_constant_int, new_constant_float, new_constant_longdouble,
    new_constant_char, new_constant_wchar, new_constant_char_p,
    new_constant_wchar_p, new_constant_pointer, new_constant_struct,
    new_constant_union, new_constant_enum, new_constant_enum_custom,
    new_constant_array, new_constant_
