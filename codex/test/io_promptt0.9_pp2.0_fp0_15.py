import io
# Test io.RawIOBase
# This file docstring will show up in help(cStringIO)

buf = None

def check_args(funcname, *args, **kwargs):
    if buf is None:
        raise ValueError("I/O operation on closed file")

class _cStringIO(io.RawIOBase):
    """A dummy raw io implementation."""
    def __init__(self, initial_value=b""):
        self._buffer = initial_value
        self._pos = 0

    @property
    def closed(self):
        """Returns True if the file is closed."""
        return self._buffer is None

    def close(self):
        """Close the file."""
        self._buffer = None

    def seek(self, pos, whence=0):
        """Seek to the given position."""
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if whence == 0:
            self._pos = pos
        elif whence == 1:
            self._pos += pos
        elif whence == 2:
            self._pos
