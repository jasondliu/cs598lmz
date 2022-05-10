import io
class File(io.RawIOBase):
    """A file-like object that reads from a given socket.

    The socket must be in non-blocking mode; typically, a :class:`Socket`
    object is used.

    File objects are not safe to share between processes.
    """

    def __init__(self, socket):
        self._socket = socket
        self._buffer = []
        self._read_bytes = 0
        self._read_from_socket()

    def _read_from_socket(self):
        # Read data from the socket, until we get EWOULDBLOCK or equivalent.
        try:
            data = self._socket.recv(4096)
        except socket.error as e:
            if errno_from_exception(e) in _ERRNO_WOULDBLOCK:
                return
            raise
        if data:
            self._buffer.append(data)
            self._read_bytes += len(data)
        else:
            # If we read an empty string, the connection has been closed.
            self._socket = None

    def readable(self):
        return True

   
