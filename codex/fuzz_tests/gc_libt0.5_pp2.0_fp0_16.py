import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, FFIError,
    _getintp_ctype, _copy_ctype, _typeof, _cdata, _CData,
    _sizeof, _alignof, _string, _wstring, _buffer, _bytes,
    _cast, _typeof_cache, _environ_config, _num_of_types,
    _backendcapi, _parse_c_type, _cffi_from_c_type,
    _backend, _cffi_exports)
from . import model
from .model import (
    CType, CTypePrimitiveType, CTypeArray, CTypePointer, CTypeFunc,
    CTypeEnum, CTypeStructOrUnion, CTypeFuncPtr, CTypeQualifier,
    CTypeEllipsis, CTypeVoid, CTypeUnknown, CTypeNull, CTypeKind,
    CTypes, CTypePtrTo, CTypeConstant,
