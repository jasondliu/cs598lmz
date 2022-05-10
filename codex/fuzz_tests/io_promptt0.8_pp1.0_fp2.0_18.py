import io
# Test io.RawIOBase and io.BufferedIOBase by emulating an instance with
# readinto
class RawIOTest():
    def readinto(self, buf):
        for i in range(len(buf)):
            buf[i] = i % 256
        return len(buf)
class BufferedIOTest(RawIOTest, io.BufferedIOBase):
    def readinto(self, buf):
        b = bytearray(len(buf))
        n = super().readinto(b)
        buf[:n] = b
        return n
with io.BytesIO() as output:
    with io.BytesIO(b'blah') as input:
        io.copyfileobj(input, output)
        print(output.getvalue())
import io
for c in io.DEFAULT_BUFFER_SIZE, io.FileIO.DEFAULT_BUFFER_SIZE, io.open().DEFAULT_BUFFER_SIZE:
    print(c)
import io

# Set up the test file
with io.open('sample.txt', 'w') as f:
    f
