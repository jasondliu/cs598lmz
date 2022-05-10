import io
# Test io.RawIOBase

import _io

class TestRawIO(_io.RawIOBase):
    def __init__(self):
        self._read_stack = []
        self._write_stack = []
        self._seek_stack = []
        self._tell_stack = []

    def readinto(self, b):
        self._check_closed()
        self._read_stack.append(b)
        return len(b)

    def write(self, b):
        self._check_closed()
        self._write_stack.append(b)
        return len(b)

    def seekable(self):
        self._check_closed()
        return True

    def seek(self, pos, whence=0):
        self._check_closed()
        self._seek_stack.append((pos, whence))

    def tell(self):
        self._check_closed()
        self._tell_stack.append(None)
        return 0

    def close(self):
        self._closed = True
        self._read_stack.append(None)
        self._write_stack
