import gc, weakref

from . import _constants as constants
from . import _errors as errors
from . import _util as util
from . import _types as types

from . import _cffi_backend as cffi_backend
from . import _ctypes_backend as ctypes_backend

import _libsodium as c

__all__ = [
    'sodium_init',
    'sodium_increment',
    'sodium_add',
    'sodium_compare',
    'sodium_memcmp',
    'sodium_is_zero',
    'sodium_memzero',
    'sodium_mlock',
    'sodium_munlock',
    'sodium_mprotect_noaccess',
    'sodium_mprotect_readonly',
    'sodium_mprotect_readwrite',
    'sodium_allocarray',
    'sodium_alloc',
    'sodium_malloc',
    'sodium_free',
    'sodium_malloc_zero',
    'sodium_allocarray_
