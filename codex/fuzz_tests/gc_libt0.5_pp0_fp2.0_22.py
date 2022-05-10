import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type,
    typeof, sizeof, alignof,
    addressof, cast, cast_ptr_to_int, cast_int_to_ptr,
    string, unpack, unpack_from, pack, pack_into,
    new, gcp, memmove,
    NULL, CData,
    CFuncPtr,
    CConstant,
    CType,
    CTypePtrOrArray,
    CTypeArray,
    CTypePrimitive,
    CTypeEnum,
    CTypeStructOrUnion,
    CTypeStruct,
    CTypeUnion,
    CTypesError,
    getcname,
    get_errno, set_errno,
    getwinerror, setwinerror,
    cdef, d
