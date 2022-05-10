import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type,
    new_void_type, new_function_type,
    new_raw_api,
    typeof, sizeof, alignof,
    cast, addressof,
    string, unpack, unpack_from, pack, pack_into,
    new, gc,
    CData, CField, CConstant,
    CDataOwning, CDataOwningGC,
    CDataGCP,
    CData_c_byte, CData_c_ubyte,
    CData_c_short, CData_c_ushort,
    CData_c_int, CData_c_uint,
    CData_c_long, CData_c_ulong,
    CData_c_longlong, CData_
