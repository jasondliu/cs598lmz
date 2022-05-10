import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_function_type_with_var_arg, new_cdata, newp, cast,
    typeof, sizeof, alignof, addressof,
    callback, getctype, getcname,
    gcp, gc,
    string, wstring, buffer,
    memmove, memset,
    set_source, set_errno, get_errno,
    getwinerror, setwinerror,
    string_at, wstring_at, buffer_at,
    string_at_raw, wstring_at_raw, buffer_at_raw,
    string_from_buffer, wstring_from_buffer,
    string_from_buffer_copy, wstring_from
