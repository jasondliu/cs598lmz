import gc, weakref
from itertools import count
from datetime import datetime
import time
from collections import namedtuple
from contextlib import contextmanager

from . import _core, _util
from ._core import ffi, lib
from ._util import (
    _bytes_from_buffer, _bytes_to_buffer, _buffer_from_bytes,
    _buffer_to_bytes, _buffer_from_unicode, _buffer_to_unicode,
    _check_closed, _check_not_closed, _check_nonzero, _check_zero,
    _ffi_check, _ffi_guard, _filename_to_bytes, _filename_from_bytes,
    _filename_to_unicode, _filename_from_unicode, _free_char_p,
    _int_from_bool, _int_to_bool, _int_to_enum, _int_from_enum,
    _int_to_size, _int_from_size, _int_to_time, _int_from_time,
    _make_enum_class, _make_int
