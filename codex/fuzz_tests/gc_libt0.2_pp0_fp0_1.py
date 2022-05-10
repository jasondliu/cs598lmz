import gc, weakref

from . import _ffi, _lib, _util
from ._util import _check_null, _check_zero, _check_one, _check_true
from ._util import _check_size, _check_type, _check_handle
from ._util import _check_errno, _check_errno_on
from ._util import _check_zero_or_ok, _check_one_or_ok
from ._util import _check_true_or_ok, _check_size_or_ok
from ._util import _check_type_or_ok, _check_handle_or_ok
from ._util import _check_errno_or_ok, _check_errno_on_or_ok
from ._util import _check_null_or_ok, _check_zero_or_ok_or_eagain
from ._util import _check_one_or_ok_or_eagain, _check_true_or_ok_or_eagain
from ._util import _check_size_or_ok_or_eagain, _check_type_or_ok_or
