import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_raw_type, new_pointer_type, new_cdata, newp, cast,
    typeof, sizeof, alignof, addressof,
    callback, getctype,
    string, wstring, array, struct, union, enum,
    gc,
    CDataOwningGC,
    CData,
    CDataMeta,
    CType,
    CTypePrimitive,
    CTypeArray,
    CTypePointer,
    CTypeFunc,
    CTypeEnum,
    CTypeStructOrUnion,
    CTypeStruct,
    CTypeUnion,
    CTypeVoid,
    CTypeVoidP,
    CTypeChar,

