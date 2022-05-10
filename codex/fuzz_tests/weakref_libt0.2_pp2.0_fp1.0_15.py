import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type, new_typedef,
    get_errno, set_errno,
    callback,
    _typeof, _sizeof, _alignof, _offsetof, _rawaddressof,
    _encode_pointer, _decode_pointer,
    _cast, _string, _buffer, _memmove, _memset,
    _memmove_addr, _memset_addr,
    _CData, _CDataMeta, _CDataOwningMeta, _CDataOwning,
    _CDataNewOwning, _CDataNewOwningMeta,
    _CDataNew, _CDataNewMeta,
    _C
