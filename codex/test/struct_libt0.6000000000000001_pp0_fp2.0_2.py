import _struct

from . import _common


class _Buffer:
    def __init__(self, size):
        self._size = size
        self._buffer = memoryview(bytearray(size))

    def read(self, n):
        n = min(n, self._size)
        self._size -= n
        return self._buffer[:n]


def _read_file_header(fp):
    """Read a file header from the given file.
    """
    fh = _common._FileHeader()
    fh.start_of_file = fp.tell() - 8

    buf = fp.read(28)
    if len(buf) < 28:
        raise EOFError("Unexpected EOF reading file header")
