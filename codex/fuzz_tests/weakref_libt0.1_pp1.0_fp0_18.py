import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type,
    new_void_type, new_function_type, new_function_type_with_var_arg,
    new_raw_api,
    _typeof, sizeof, alignof,
    cast, addressof,
    gc,
    CData, CType, CConstant,
    _CDataMeta, _CDataOwningMeta,
    _CDataOwning, _CDataOwning_Output, _CDataOwning_Output_Owned,
    _CData_Output, _CData_Output_Owned,
    _CData_retval, _CData_retval_owning,
    _CData_nonconverting, _CData_nonconverting_owning,
    _CData_nonconverting_
