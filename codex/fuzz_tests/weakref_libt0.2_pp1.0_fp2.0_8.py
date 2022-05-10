import weakref

from . import _core
from . import _util
from . import _errors
from . import _types
from . import _constants
from . import _lib
from . import _ffi
from . import _raw
from . import _compat
from . import _version

__all__ = [
    'open',
    'open_memstream',
    'open_buffer',
    'open_buffer_read',
    'open_buffer_write',
    'open_buffer_rw',
    'open_fd',
    'open_callbacks',
    'open_file',
    'open_filename',
    'open_filename_utf8',
    'open_filename_w',
    'open_pipe',
    'open_process',
    'open_process_read',
    'open_process_write',
    'open_process_rw',
    'open_process_full',
    'open_socket',
    'open_socket_read',
    'open_socket_write',
    'open_socket_rw',
    'open_
