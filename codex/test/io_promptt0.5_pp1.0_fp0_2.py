import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return "".encode('utf-8')

try:
    io.RawIOBase.readall
except AttributeError:
    pass
else:
    print("io.RawIOBase.readall exists")

try:
    io.RawIOBase.readinto1
except AttributeError:
    pass
else:
    print("io.RawIOBase.readinto1 exists")

try:
    io.RawIOBase.readinto
except AttributeError:
    print("io.RawIOBase.readinto doesn't exist")
else:
    print("io.RawIOBase.readinto exists")

try:
    io.RawIOBase.read1
except AttributeError:
    pass
else:
    print("io.RawIOBase.read1 exists")

try:
    io.RawIOBase.read
except AttributeError:
    print("io.RawIOBase.read doesn't exist")
