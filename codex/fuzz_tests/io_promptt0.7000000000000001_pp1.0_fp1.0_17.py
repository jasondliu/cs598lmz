import io
# Test io.RawIOBase
class _FakeRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n
    def write(self, b):
        pass
class _CustomIOBase(_io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n
    def write(self, b):
        pass
class _BatchedIOBase(_io.RawIOBase):
    def readinto(self, b):
        return len(b)
    def write(self, b):
        pass
class _SubclassIOBase(_io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n
    def write(self, b):
        pass
class _ReadonlyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n
class _WriteonlyRawIO(_io.RawIOBase):
    def write(self, b):
        pass

class _FakeIOBase(_
