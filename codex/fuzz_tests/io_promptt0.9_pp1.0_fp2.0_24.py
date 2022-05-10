import io
# Test io.RawIOBase
mem = io.BytesIO()

class memory(io.RawIOBase):
    def readinto(self, b: bytes) -> int:
        m.seek(len(b))
        return len(b)

    def write(self, b: bytes) -> int:
        m.write(b)
        return len(b)

m = memory()
m.write(b'abc')
m.seek(0)
s = m.read(1)
print(s)
s = m.read(2)
print(s)
s = m.read(1)
print(s)
m.seek(0, io.SEEK_SET)
s = m.read(1)
print(s)
s = m.read(2)
print(s)
s = m.read(1)
print(s)
m.write(b'Hello')
m.seek(0)
s = m.read()
print(s)
m.seek(0)
buffers = []
for i in range(10):
    buffers.append(b
