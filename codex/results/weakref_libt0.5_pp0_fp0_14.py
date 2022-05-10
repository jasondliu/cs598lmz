import weakref

from . import (
    _cffi_backend,
    _ctypes_backend,
    _cython_backend,
    _dummy_backend,
    _multiprocessing,
)
from ._utils import get_shared_lib_extension

_backend_state = None
_backend_lock = _multiprocessing.Lock()

# Cached reference to the current backend.
_backend = None

# Cached reference to the current backend's Backend class.
_Backend = None

# Cached reference to the current backend's Backend class, but with a
# different name.
_backend_class = None

# Cached reference to the current backend's Backend class, but with a
# different name.
_backend_cls = None

# Cached reference to the current backend's Backend class, but with a
# different name.
_backend_class_name = None

# Cached reference to the current backend's Backend class, but with a
# different name.
_backend_
