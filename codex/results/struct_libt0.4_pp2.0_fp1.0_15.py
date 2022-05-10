import _struct

from . import _cffi_backend


def _get_ffi_type(t):
    if isinstance(t, _cffi_backend.CData):
        return t._ffi_type
    if isinstance(t, _cffi_backend.CType):
        return t._get_ffi_type()
    if isinstance(t, _cffi_backend.CTypePtrOrArray):
        return t._get_ffi_type()
    if isinstance(t, _cffi_backend.CTypeFuncPtr):
        return t._get_ffi_type()
    if isinstance(t, _cffi_backend.CTypeStructOrUnion):
        return t._get_ffi_type()
    if isinstance(t, _cffi_backend.CTypeEnum):
        return t._get_ffi_type()
    if isinstance(t, _cffi_backend.CTypePrimitive):
        return t._get_ffi_type()
    raise
