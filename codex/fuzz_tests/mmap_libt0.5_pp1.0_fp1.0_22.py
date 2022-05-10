import mmap
import os
import re
import sys

from . import _cffi_backend
from . import _ctypes_backend
from . import _cython_backend
from . import _dlfcn_backend
from . import _fake_backend
from . import _framework_backend
from . import _memimporter
from . import _util
from ._util import (
    basestring,
    byte,
    bytes,
    bytearray,
    unicode,
    string_types,
    text_type,
    binary_type,
    PY2,
    PY3,
    is_py3,
    is_py2,
    is_win,
    is_darwin,
    is_linux,
    is_freebsd,
    is_sunos,
    is_aix,
    is_cygwin,
    is_pypy,
    is_jython,
)

#: The default backend to use.
DEFAULT_BACKEND = "auto"

#: The set of valid
