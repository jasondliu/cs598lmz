import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_raw_api, new_type_from_opaque_pointer,
    typeof, sizeof, alignof,
    callback,
    string,
    getcname,
    gcp, gc_weakref,
    _typeof, _sizeof, _alignof,
    _backendutil,
    _num_to_raw, _raw_to_num,
    _CData, _CDataMeta, _CDataOwningMeta,
    _CDataOwning, _CDataGCP, _CDataWeakRef,
    _CDataMem, _CDataMemInfo,
    _CData_input_not_acceptable,
    _CData_output_
