import io
class File(io.RawIOBase):
    def write(self, b):
        print(b)
        return len(b)

f = File()
print(f.write(b'abc'))
print(f.write(b'def'))
print(f.write(b'ghi'))

print(f.isatty())
print(f.readable())
print(f.writable())
print(f.seekable())

print(f.close())

print(f.write(b'xyz'))
