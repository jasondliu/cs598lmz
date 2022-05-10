import _struct

from . import _cffi_backend
from . import _ctypes_backend
from . import _cython_backend
from . import _ctypes_backend_libffi
from . import _cffi_backend_ctypes
from . import _cffi_backend_libffi


def _get_backend_name(backend):
    if backend is None:
        return None
    if backend == 'default':
        return None
    if backend == 'ctypes':
        return 'ctypes'
    if backend == 'cffi':
        return 'cffi'
    if backend == 'cython':
        return 'cython'
    if backend == 'libffi':
        return 'libffi'
    raise ValueError("invalid backend name: %r" % (backend,))


def _get_backend_module(backend):
    if backend is None:
        return _cffi_backend
    if backend == 'ctypes':
        return _ctypes_backend
    if
