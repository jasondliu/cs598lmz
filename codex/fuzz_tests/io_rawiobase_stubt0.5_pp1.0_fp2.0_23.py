import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"a"*n

f = File()
f.read()

print(f.read(5))

print(f.readinto(bytearray(5)))
print(f.readinto1(bytearray(5)))

print(f.readinto(memoryview(bytearray(5))))

# print(f.readinto1(memoryview(bytearray(5))))

print(f.read1(5))

print(f.readinto1(b" "*5))

# print(f.readinto1(memoryview(b" "*5)))
