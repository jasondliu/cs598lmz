import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

import sys
if sys.version_info[0] == 2:
    from StringIO import StringIO
    File.StringIO = StringIO
else:
    from io import StringIO
    File.StringIO = StringIO

class FileObject(object):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        return self.file.write(b)
    def close
