import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, handle_from_ptr, handle_from_buffer,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type,
    typeof, sizeof, alignment,
    cast, addressof, byref,
    callback,
    string, wstring,
    buffer,
    _typeof, _sizeof, _alignment,
    _cast, _addressof, _byref,
    _string, _wstring,
    _buffer,
    _backendutil,
    _CData, _CDataMeta,
    _CDataOwning, _CDataOwningMeta,
    _CDataOwningGCP, _CDataOwningGCPMeta,
    _CDataGCP, _CDataGCPMeta,
    _CDataGC, _CDataGCMeta,
    _make_gcp, _make
