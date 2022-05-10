import io
# Test io.RawIOBase.readline

import _io

class MockRawIO(_io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, buf):
        raise NotImplementedError

try:
    MockRawIO().readline()
except TypeError:
    print('SKIP')
    raise SystemExit

class MockRawIO2(MockRawIO):
    def readinto(self, buf):
        data = b'1234567890abcdef'
        l = min(len(data), len(buf))
        buf[:l] = data[:l]
        return l

buf = bytearray(5)
m = MockRawIO2()
print(m.readinto(buf))
print(buf)
print(m.readinto(buf))
print(buf)
