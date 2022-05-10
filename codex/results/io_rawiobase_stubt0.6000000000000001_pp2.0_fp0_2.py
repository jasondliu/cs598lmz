import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file

    def readall(self):
        return self.file.read()

    def read(self, n=-1):
        return self.file.read(n)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset)

    def tell(self):
        return self.file.tell()

# These functions are for internal use only
def _read_bytes(file, offset, length):
    if not isinstance(file, File):
        file = File(file)
    file.seek(offset)
    return file.read(length)

def _write_bytes(file, offset, data):
    if not isinstance(file, File):
        file = File(file)
    file.seek(offset)
    file.write(data)

def _pad_to(file, offset, length):
    if not isinstance(file, File
