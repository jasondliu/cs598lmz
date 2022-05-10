import gc, weakref

from . import _base
from ._base import _as_parameter_
from . import _ctypes
from ._ctypes import _SimpleCData, _CData, CFuncPtr, _Pointer, Structure, Union
from . import _rawffi
from ._rawffi import (sizeof, alignment, get_errno, set_errno,
                      get_last_error, set_last_error,
                      FFIError,
                      CDLL, RTLD_LOCAL, RTLD_GLOBAL, RTLD_NOW,
                      get_libc_name, get_libc_name_encoding,
                      get_errno_location, get_last_error_location,
                      get_default_error_return,
                      Array, Data_size, addressof,
                      CConfig, CConstant, CExternVariable,
                      CCompiledLib, CCompiledFunction,
                      CCompiledType,
                      _CDataMeta,
                      _CDataMeta_output,
                      _CDataMeta_input,
                      _CDataMeta_output_noerrcheck,

