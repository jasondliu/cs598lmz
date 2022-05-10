import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return 0

    def write(self, b):
        return 0

r = RawI()
r.readable()
r.writable()
r.seekable()
r.readinto(b"")
r.write(b"")

# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return 0

    def write(self, b):
        return 0

b = BufferedI()
b.readable()
b.writable()
b.seekable()
b.readinto(b"")
b.write(b"")

# Test io.TextIOBase
class TextI(
