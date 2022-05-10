import io
class File(io.RawIOBase):
    def __init__(self, filepath, *args, **kwargs):
        self.file = open(filepath, *args, **kwargs)
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def write(self, b):
        return self.file.write(b)
    def writable(self):
        return True
    def writelines(self, lines):
        return self.file.writelines(lines)
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()

#=====================================================================
#
#   class:  File
#
#   A file object that can be used
