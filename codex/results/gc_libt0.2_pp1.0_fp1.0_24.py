import gc, weakref

from . import _util, _compat, _constants, _errors, _ffi
from ._errors import _make_error, _make_oserror
from ._util import _check_closed
from ._compat import integer_types, PY2, PY3, text_type, binary_type
from ._constants import (
    _DEFAULT_BUFFER_SIZE, _DEFAULT_ENCODING, _DEFAULT_ERROR_HANDLING,
    _DEFAULT_NEWLINE, _DEFAULT_TEXT_MODE, _DEFAULT_UNIVERSAL_NEWLINE,
    _DEFAULT_LINE_BUFFERING, _DEFAULT_WRITE_THROUGH, _DEFAULT_RAW_MODE,
    _DEFAULT_BUFFERED_MODE, _DEFAULT_OPEN_MODE, _DEFAULT_OPEN_FLAGS,
    _DEFAULT_OPEN_RETRIES, _DEFAULT_OPEN_RETRY_DELAY, _DEFAULT_OPEN_TIMEOUT,
    _DEFAULT_OPEN_BACKUP_COUNT, _DEFAULT_OP
