import io
# Test io.RawIOBase with a file object


class WrapperIO(io.RawIOBase):

    def __init__(self, f):
        self.f = f

    def read(self, *args, **kwargs):
        return self.f.read(*args, **kwargs)

    def write(self, *args, **kwargs):
        return self.f.write(*args, **kwargs)

    def readable(self):
        return self.f.readable()

    def writable(self):
        return self.f.writable()

    def close(self):
        self.f.close()


