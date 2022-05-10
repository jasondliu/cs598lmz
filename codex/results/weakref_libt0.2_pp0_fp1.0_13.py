import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type,
    new_cdata, cast, typeof, sizeof, alignof,
    addressof, getcname, string, unpack, unpack_from, pack, pack_into,
    CDataOwning, CData,
    gcpython_api, gcpython_make_finalizer,
    gcpython_raw_address, gcpython_raw_ref, gcpython_raw_ptr,
    gcpython_raw_callable, gcpython_raw_struct,
    gcpython_raw_new_allocator, gcpython_raw_new_with_finalizer,
    gcpython_raw_new_
