import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type, new_typedef,
    new_constant_int, new_constant_float, new_constant_char,
    new_global_var, new_global_const,
    new_c_function, new_c_function_var, new_c_function_const,
    new_c_function_raw, new_c_function_var_raw, new_c_function_const_raw,
    new_c_function_raw_exn, new_c_function_var_raw_exn,
    new_c_function_const_raw_exn,
    new_c_function_exn, new_
