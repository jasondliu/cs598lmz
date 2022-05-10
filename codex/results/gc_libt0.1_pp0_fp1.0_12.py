import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type, new_void_type,
    new_function_type, new_raw_union_type, new_raw_struct_type,
    new_fused_c_struct_type, new_fused_c_struct_as_union_type,
    new_fused_c_struct_as_opaque_type, new_fused_c_struct_as_opaque_union_type,
    new_fused_c_struct_as_opaque_struct_type,
    new_fused_c_struct_as_opaque_struct_union_type,
    new_fused_c_struct_as_opaque_struct_p_type,
    new_fused_c_struct_as_opaque_struct_p_union_type,
    new_f
