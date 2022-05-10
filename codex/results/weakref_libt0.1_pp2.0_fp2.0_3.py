import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type, new_type_from_opaque_pointer,
    new_type_from_handle, new_type_from_enum_type, new_type_from_struct_type,
    new_type_from_union_type, new_type_from_pointer_type,
    new_type_from_array_type, new_type_from_function_type,
    new_type_from_void_type, new_type_from_primitive_type,
    new_type_from_c_function, new_type_from_c_function_pointer,
    new_type_from_c_function_pointer_and_name,

