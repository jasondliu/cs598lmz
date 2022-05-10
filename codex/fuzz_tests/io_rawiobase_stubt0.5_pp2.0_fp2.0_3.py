import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self._file = open(filename, 'rb')

    def read(self, size=-1):
        return self._file.read(size)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()

with File('/etc/passwd') as f:
    print(f.read())

# io.StringIO
# io.BytesIO

# io.StringIO is an in-memory stream for text I/O.
# It inherits io.TextIOBase.

# io.BytesIO is an in-memory stream for binary I/O.
# It inherits io.BufferedIOBase.

# StringIO can accept either unicode or str strings,
# but mixing the two may take some care.
# BytesIO is intended to receive str strings,
# but can accept unicode
