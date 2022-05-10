import io
# Test io.RawIOBase
class test_RawIOBase:

    def write(self, b):
        io.RawIOBase.write(self, b)
        io.RawIOBase.flush(self)


