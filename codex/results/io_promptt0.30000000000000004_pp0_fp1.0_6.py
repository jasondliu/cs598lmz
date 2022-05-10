import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n

rawio = MyRawIO()
print(rawio.read(10))
# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b'x' * n

bufferedio = MyBufferedIO()
print(bufferedio.read(10))
# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=-1):
        return 'x' * n

textio = MyTextIO()
print(textio.read(10))
# Test io.FileIO
fileio = io.FileIO('test.txt', 'w')
fileio.write(b'abc')
fileio.close()
# Test io.BytesIO
bytesio = io.BytesIO()
bytesio.write(b'abc')
print(bytesio.getvalue())
# Test io.StringIO
