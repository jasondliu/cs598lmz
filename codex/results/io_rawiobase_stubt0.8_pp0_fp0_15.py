import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return "Not Implemented"
    def write(self, b):
        return NotImplemented
with File() as f:
    print(f.read())



class File(io.RawIOBase):
    def read(self, size=-1):
        return b"Not Implemented"
    def write(self, b):
        return NotImplemented
with File() as f:
    print(f.read())



from contextlib import suppress
class File(io.RawIOBase):
    def read(self, size=-1):
        raise NotImplementedError("Not Implemented")
with suppress(NotImplementedError):
    with File() as f:
        print(f.read())
