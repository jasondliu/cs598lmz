import weakref

from . import _lib
from . import _ffi
from . import _core
from . import _error
from . import _compat
from . import _util

from . import _collections

from . import _libsodium
from . import _openssl
from . import _cffi
from . import _cffi_backend
from . import _cryptography


_available_backends = [_libsodium, _openssl, _cffi, _cryptography]

if _core.PYVER >= (3, 5):
    _available_backends.append(_cffi_backend)

_backend = None

_backend_initialized = False

_backend_lock = _util.threading.Lock()


def _get_backend():
    global _backend
    global _backend_initialized

    if _backend_initialized:
        return _backend

    _backend_lock.acquire()

    try:
        if _backend_initialized:
            return _backend

        for backend in _available
