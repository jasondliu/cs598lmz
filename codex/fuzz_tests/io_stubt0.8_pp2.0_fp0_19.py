import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
f = io.BufferedReader(File())
f.read(3)
del f
print(view)
f = io.BufferedReader(File())
f.read(10)
del f
print(view)

# Test that a BufferedReader with a readinto method is compatible with
# io.BytesIO.
class C:
    def readinto(self, buf):
        buf[:] = b"foo bar baz"
        return len(buf)

with BytesIO(b"") as impl:
    with BufferedReader(C()) as buf:
        content = buf.read(7)
        impl.write(b"cou")
        impl.write(b"cou")
        content += buf.read()
        impl.write(b"cou")
        impl.write(b"cou")
    print(content)

# BytesIO with explicit 0-length buffer
with io.BytesIO(b"") as b:
    print(b.write(b""))
    print(b.seek(0))

