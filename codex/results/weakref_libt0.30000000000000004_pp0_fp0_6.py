import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, get_handle, get_type_raw, get_exception_raw,
    get_string_raw, get_struct_raw, get_array_raw, get_union_raw,
    get_enum_raw, get_function_raw, get_global_raw,
    get_callback_raw, get_pointer_raw, get_primitive_type,
    get_null_ptr_type, get_int_type, get_void_ptr_type,
    get_const_string_type, get_int_size, get_alignment,
    get_errno, set_errno,
    FFIError, VerificationError,
    FFI, CDefError, CType, CTypeDescr, CConstant,
    CField, CStructOrUnion, CStruct, CUnion,
    CArray, CEnum, CExternVariable, CExternFunction,
    CTypeOf, CArrayOf, CPointerTo, CFixedArray,
