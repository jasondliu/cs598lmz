import weakref

from . import constants as c
from . import utils

from . import _cffi_backend
from ._cffi_backend import (
    _cdata, _rawffi, _copy_ctype_to_cdata, _copy_cdata_to_ctype,
    _cdata_needs_free, _cdata_is_nonzero, _cdata_is_simple_type,
    _cdata_is_array, _cdata_is_struct, _cdata_is_union, _cdata_is_enum,
    _cdata_is_void_ptr, _cdata_is_ptr_to_void, _cdata_is_ptr_to_function,
    _cdata_is_ptr_to_function_or_void, _cdata_is_ptr_to_struct,
    _cdata_is_ptr_to_struct_or_void, _cdata_is_ptr_to_array,
    _cdata_is_ptr_to_array_or_void, _cdata_is_ptr_
