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
