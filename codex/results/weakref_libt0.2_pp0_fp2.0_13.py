import weakref
import logging

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type,
    new_void_type, new_function_type, new_function_type_with_var_arg,
    new_type_from_opaque_pointer,
    typeof, sizeof, alignof,
    cast, addressof,
    gcp, gc_ref, gc_unref,
    typeoffsetof,
    offsetof,
    getcname,
    string,
    buffer,
    from_handle,
    callback,
    load_library,
    dlopen,
    dlclose,
    dlsym,
    dlerror,
    get_errno,
    set_errno,
    getwinerror,
    setwinerror,
    get_last_error,
    set
