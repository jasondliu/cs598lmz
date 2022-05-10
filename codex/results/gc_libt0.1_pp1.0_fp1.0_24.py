import gc, weakref

from . import _util
from ._util import _get_c_funcs

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_funcptr_type,
    cast, cast_ptr_to_int, cast_int_to_ptr,
    string, unpack, unpack_from, pack, pack_into,
    sizeof, alignof, typeof,
    addressof, byref,
    new, newp,
    gcp, gc_custom,
    callback,
    CData, CDataOwning,
    CDataMeta,
    _CDataMeta,
    _CDataOwning,
    _CDataMeta_output,
    _CDataMeta_output_no_keepalive,
    _CDataMeta_nonconforming,
    _CDataMeta_non
