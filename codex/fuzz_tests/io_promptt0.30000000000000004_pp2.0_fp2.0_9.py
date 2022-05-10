import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        return b"\x00" * size

rawio = MyRawIO()
print(rawio.read(10))
# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def read(self, size=-1):
        return b"\x00" * size

bufferedio = MyBufferedIO()
print(bufferedio.read(10))
# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, size=-1):
        return "0" * size

textio = MyTextIO()
print(textio.read(10))
# Test io.FileIO
# fileio = io.FileIO("file.txt", "w")
# fileio.write(b"Hello World")
# fileio.close()
# fileio = io.FileIO("file.txt", "r")
# print(fileio.read())
# fileio.close()

