import io
# Test io.RawIOBase.readall()

class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.len = 0

    def readable(self):
        return True

    def readinto(self, buf):
        self.len += len(buf)
        return len(buf)

rawio = MyRawIO()
rawio.readall()
rawio.readall()
rawio.readall()
print(rawio.len)
