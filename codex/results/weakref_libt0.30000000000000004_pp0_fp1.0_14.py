import weakref

from . import _lib
from ._lib import ffi, lib

from . import _util
from ._util import _check_null, _check_zero

from . import _error
from ._error import _make_error_from_c_error, _make_error_from_getaddrinfo_errno, _make_error_from_errno


class _Socket(object):
    """Base class for sockets."""

    def __init__(self, sock):
        self._sock = sock

    def __del__(self):
        if self._sock is not None:
            _check_zero(lib.uv_close(self._sock))

    def fileno(self):
        return lib.uv_fileno(self._sock)

    def getsockname(self):
        """Get the socket name.

        Returns:
            A tuple of (ip, port).
        """
        name = ffi.new("struct sockaddr_storage*")
        namelen = ffi.new("int*")
        _check_zero(lib.uv_
