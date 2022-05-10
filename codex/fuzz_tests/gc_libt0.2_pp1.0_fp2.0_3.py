import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, new_handle, addressof, sizeof, alignment, buffer, cast,
    string, unpack, _typeof, _backendutil, _rawffi,
    _copy_ctype_to_cdata, _copy_cdata_to_ctype, _cdata_is_object,
    _cdata_is_struct, _cdata_is_union, _cdata_is_array, _cdata_is_enum,
    _cdata_is_primitive, _cdata_is_pointer, _cdata_is_function,
    _cdata_is_void_ptr, _cdata_is_nonfunc_pointer, _cdata_is_longdouble,
    _cdata_is_float, _cdata_is_double, _cdata_is_int, _cdata_is_longlong,
    _cdata_is_ulonglong, _cdata_is_long, _cdata_is_ulong, _
