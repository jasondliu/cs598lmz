import io
class File(io.RawIOBase):
    """
    Fake file object used to check the value returned by the
    file.open builtin
    """
    def __init__(self, bufsize=0, mode=None):
        self.bufsize = bufsize
        self.mode = mode

    def writable(self):
        return 'w' in self.mode
    def readable(self):
        return 'r' in self.mode
    def seekable(self):
        return 'r' in self.mode

    def open(self, file, mode=None):
        return File(self.bufsize, mode)

    def read(self, n=-1):
        return self.mode

    def write(self, b):
        return 0


# Redefine open builtin

builtins.open = File().open

# Import packages to test
import os
import os.path

# List packages to test
packages = ["datetime", "sys", "subprocess", "io", "struct", "json", "hashlib",
            "base64", "ctypes", "xml", "re", "zlib",
