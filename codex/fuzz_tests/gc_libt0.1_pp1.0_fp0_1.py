import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_raw_api, new_type_from_opaque_pointer,
    typeof, sizeof, alignof,
    callback,
    addressof, cast, string,
    gcp, gc_move, gc_move_n, gc_move_a, gc_move_a_n,
    gc_realloc, gc_free, gc_free_atomic,
    gc_set_max_heap_size, gc_get_max_heap_size, gc_get_free_space,
    gc_get_total_space, gc_get_max_heap_size_from_env,
    gc
