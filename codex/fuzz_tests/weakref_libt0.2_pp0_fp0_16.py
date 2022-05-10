import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type,
    new_void_type, new_function_type,
    add_type_to_module,
    _typeof, sizeof, alignment, typeoffsetof,
    cast, cast_ptr_to_int, cast_int_to_ptr,
    string, unpack, unpack_from, pack, pack_into,
    new, addressof,
    callback,
    CConstant, CConstantInt, CConstantFloat, CConstantPointer,
    CConstantArray, CConstantStruct, CConstantUnion, CConstantEnum,
    CConstantVoid, CConstantFunction,
    CConstantCharArray, CConstantWCharArray,
    CConstantString, CConstantWString,
    CCon
