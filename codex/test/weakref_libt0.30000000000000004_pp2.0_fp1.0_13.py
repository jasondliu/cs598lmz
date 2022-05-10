import weakref
import threading
import time
from collections import defaultdict
from functools import wraps
from contextlib import contextmanager

from . import _util
from ._util import _PY3, _PY35, _PY36, _PY37, _PY38, _PY39, _PYPY, _WIN, _LINUX, _MAC, _POSIX, _UNIX, _DARWIN, _BSD, _AIX, _SOLARIS, _CYGWIN, _MSYS, _INTERRUPTED_EXCEPTIONS, _TIMEOUT_MAX, _TIMEOUT_MAX_INT64, _TIMEOUT_MAX_FLOAT, _TIMEOUT_MAX_FLOAT32, _TIMEOUT_MAX_FLOAT64, _TIMEOUT_MAX_FLOAT128, _TIMEOUT_MAX_FLOAT256, _TIMEOUT_MAX_FLOAT512, _TIMEOUT_MAX_FLOAT1024, _TIMEOUT_MAX_FLOAT2048, _TIMEOUT_MAX_FLOAT4096, _TIMEOUT_MAX_FLOAT8
