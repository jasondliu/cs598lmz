import io
class File(io.RawIOBase):
    def read(self, n=-1):
        with self._open() as f:
            return f.read(n)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        with self._open() as f:
            return f.seek(offset, whence)

    def tell(self):
        with self._open() as f:
            return f.tell()

    def write(self, b):
        with self._open() as f:
            return f.write(b)

    def writable(self):
        return True


class S3File(File):
    def __init__(self, bucket_name, path, s3hook=None):
        super().__init__()
        self.bucket_name = bucket_name
        self.path = path
        self.s3hook = s3hook
        if self.s3hook is None:
            self.s3hook = S3Hook()

    def _open(self):
        return self.
