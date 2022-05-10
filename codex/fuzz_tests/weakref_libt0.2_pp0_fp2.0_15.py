import weakref

from . import _ffi as ffi, _lib as lib, _util as util
from ._util import _check_null, _check_zero, _check_nonzero, _check_one
from ._util import _check_true, _check_false, _check_nullable, _check_nonnull
from ._util import _check_handle, _check_not_closed, _check_closed
from ._util import _check_int_ge, _check_int_gt, _check_int_le, _check_int_lt
from ._util import _check_int_eq, _check_int_ne, _check_int_in
from ._util import _check_bytes, _check_bytes_or_none, _check_bytes_or_unicode
from ._util import _check_unicode, _check_unicode_or_none, _check_unicode_or_bytes
from ._util import _check_unicode_or_int, _check_unicode_or_int_or_none
from ._util import _check_unicode_or_int_or_float,
