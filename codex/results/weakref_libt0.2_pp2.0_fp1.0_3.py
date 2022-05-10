import weakref

from .. import _core
from .. import _util
from .. import _api_internal
from .._api_internal import _to_c_string_array
from .._ffi.function import _init_api
from .._ffi.function import _init_api_ext
from .._ffi.function import _init_api_ext_with_module
from .._ffi.function import _init_api_ext_with_module_and_symbol
from .._ffi.function import _init_api_ext_with_symbol
from .._ffi.function import _init_api_ext_with_symbol_and_module
from .._ffi.function import _init_api_ext_with_symbol_and_module_and_symbol
from .._ffi.function import _init_api_ext_with_symbol_and_symbol
from .._ffi.function import _init_api_ext_with_symbol_and_symbol_and_module
from .._ffi.function import _init_api_ext_with_symbol
