import io
# Test io.RawIOBase

try:
    io.RawIOBase
except AttributeError:
    print("SKIP")
    raise SystemExit

class TestRawIO(io.RawIOBase):
    def write(self, b):
        print("write", b)
        return len(b)

    def readable(self):
        return True

    def readinto(self, b):
        print("readinto")
        return 0

print(TestRawIO().read(1))
print(TestRawIO().readinto(bytearray(1)))
print(TestRawIO().readinto(memoryview(bytearray(1))))
print(TestRawIO())
