import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"\x00" * n

class MyBytesIO(io.BytesIO):
    def read(self, n=-1):
        return b"\x00" * n

class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b"\x00" * n

class MyFileIO(io.FileIO):
    def read(self, n=-1):
        return b"\x00" * n

# Issue #17976: Check that readinto() doesn't raise an exception
# in the case where the object's read() method returns a bytes object
# of length zero.
for rawio in [MyRawIO(), MyBytesIO(), MyBufferedIO(MyRawIO()),
              MyBufferedIO(MyBytesIO()), MyBufferedIO(MyFileIO(__file__))]:
    buf = bytearray(10)
