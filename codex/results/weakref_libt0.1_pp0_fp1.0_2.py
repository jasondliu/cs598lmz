import weakref
import logging

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type,
    new_function_type, new_c_function_type, new_function_type_with_var_arg,
    new_c_function_type_with_var_arg, new_function_type_with_keywords,
    new_c_function_type_with_keywords, new_function_type_with_signature,
    new_c_function_type_with_signature, new_function_type_with_signature_and_var_arg,
    new_c_function_type_with_signature_and_var_arg, new_function_type_with_signature_and_keywords,
    new_c_function_type_with_signature_and_keywords
