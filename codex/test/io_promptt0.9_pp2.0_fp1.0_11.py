import io
# Test io.RawIOBase subclass with custom fileno() method
class FNoRawIO(io.RawIOBase):

    def __init__(self, fileno=-2):
        self._fileno = fileno

    def fileno(self):
        return self._fileno

