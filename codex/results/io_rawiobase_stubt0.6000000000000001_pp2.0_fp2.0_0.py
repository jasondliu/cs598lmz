import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n).encode()
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def writable(self):
        return True
    def write(self, b):
        return self.file.write(b.decode())
__builtins__.open = open = lambda file, mode='r', buffering=-1, encoding=None,
                           errors=None, newline=None, closefd=True, opener=None: \
                           io.open(File(file), mode, buffering, encoding, errors, newline, closefd, opener)

import subprocess
def Popen(cmd, *args, **kwargs):
    if isinstance(cmd, list):
        cmd = ' '.join(cmd
