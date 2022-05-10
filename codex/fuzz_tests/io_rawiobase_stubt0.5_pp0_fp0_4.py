import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return b'\x00' * size
    def readable(self):
        return True

# from io import RawIOBase
class File(RawIOBase):
    def read(self, size=-1):
        return b'\x00' * size
    def readable(self):
        return True

# from io import RawIOBase
class File(RawIOBase):
    def read(self, size=-1):
        return b'\x00' * size
    def readable(self):
        return True

# from io import RawIOBase
class File(RawIOBase):
    def read(self, size=-1):
        return b'\x00' * size
    def readable(self):
        return True

# from io import RawIOBase
class File(RawIOBase):
    def read(self, size=-1):
        return b'\x00' * size
    def readable(self):
        return True

# from io import RawIOBase
class File(RawIOBase):
    def read(self
