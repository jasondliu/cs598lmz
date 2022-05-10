import select
import sys

from . import exc
from . import util
from . import compat

__all__ = ["Stream", "SocketStream"]


class Stream(object):
    """
    A Stream represents an asynchronous, two-way connection to another
    process.

    This is an abstract, low-level interface.  It should not be
    necessary to call any of these methods directly except perhaps to
    implement a new Stream subclass.
    """

    def __init__(self):
        self._read_callback = None
        self._read_callback_args = None
        self._read_callback_kwargs = None

    def connect(self, address):
        """
        Connect the stream to a remote address.  Returns a Future
        which will resolve to the connected Stream.
        """
        raise NotImplementedError()

    def write(self, data):
        """
        Write data to the stream.  Returns a Future which will resolve
        when the data has been flushed to the OS buffers.
        """
        raise NotImplementedError()

    def read_bytes(self, num_bytes,
