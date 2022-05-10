import io
# Test io.RawIOBase
import io
import socket
class SocketIO(io.RawIOBase):
    def __init__(self, sock, mode):
        self.sock = sock
        self._mode = mode
        if mode == io.READ:
            self._reading = True
            self._writing = False
            self._seekable = False
        elif mode == io.WRITE:
            self._reading = False
            self._writing = True
            self._seekable = False
        elif mode == io.READ | io.WRITE:
            self._reading = True
            self._writing = True
            self._seekable = False
        else:
            raise ValueError("Invalid mode: %r" % mode)

    def readable(self):
        return self._reading

    def writable(self):
        return self._writing

    def seekable(self):
        return self._seekable

    def _checkReadable(self):
        if not self._reading:
            raise io.UnsupportedOperation("File or stream is not open for reading")

