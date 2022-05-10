import io
class File(io.RawIOBase):
    def write(self, b):
        return io.RawIOBase.write(self, b)
