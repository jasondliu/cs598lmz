import weakref

from . import _base
from . import _util
from . import _compat
from . import _constants
from . import _errors
from . import _ffi
from . import _lib
from . import _opcode
from . import _pyutil
from . import _types
from . import _util
from . import _version
from . import _vm
from . import _wasmtime

_ffi.lib.wasm_store_new.argtypes = [_ffi.wasm_engine_t]
_ffi.lib.wasm_store_new.restype = _ffi.wasm_store_t

_ffi.lib.wasm_store_delete.argtypes = [_ffi.wasm_store_t]
_ffi.lib.wasm_store_delete.restype = None
