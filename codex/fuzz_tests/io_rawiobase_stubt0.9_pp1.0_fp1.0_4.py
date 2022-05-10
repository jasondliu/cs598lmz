import io
class File(io.RawIOBase):

    def _initlize(self, f):
        self.f = f

    def read(self, n):
        return self.f.read(n)

    def seek(self, n):
        raise io.UnsupportedOperation
