import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_function_type_with_var_arg,
    new_cdata, cast, typeof, sizeof, alignof,
    addressof, getcname, string,
    callback,
    gcp, gc,
    _typeof, _sizeof, _alignof, _get_types,
    _backendutil,
    _num_to_raw_address, _raw_address_to_num,
    _CDataOwningGC, _CDataOwning, _CData_retain, _CData_release,
    _CData_is_1str, _CData_is_2str, _CData_is_3str, _CData_is_4str
