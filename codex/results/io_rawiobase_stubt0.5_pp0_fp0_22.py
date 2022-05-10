import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            r = self.file.readinto(view)
            view = view[r:]
            n -= r
        return len(b)
f = open('/dev/urandom', 'rb')
f = File(f)
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.readinto(bytearray(16))
f.
