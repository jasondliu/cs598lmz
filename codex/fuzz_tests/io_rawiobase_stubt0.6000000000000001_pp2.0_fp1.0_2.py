import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', closefd=True):
        self._file = open(filename, mode, closefd)
        self.name = filename
        self.mode = mode
    def close(self):
        self._file.close()
    def __repr__(self):
        return '<File {}>'.format(self.name)

import os
import sys

#os.close = lambda fd: None
#os.read = lambda fd, size: b'\x00'*size
#os.write = lambda fd, data: len(data)
#os.lseek = lambda fd, offset, whence: 0

#os.open = lambda path, flags, mode=0o777: 0
#os.open = lambda path, flags=os.O_RDONLY, mode=0o777, path_mode=None: 0

#os.open = lambda path, flags, mode=0o777, *, dir_fd=None: 0

#os.open = lambda path, flags, mode=0o777,
