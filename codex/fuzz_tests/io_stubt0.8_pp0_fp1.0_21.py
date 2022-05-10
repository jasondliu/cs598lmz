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

class File:
    def write(self, text):
        global read
        read = text
    def writable(self):
        return True

f = io.BufferedWriter(File())
f.write(b'\x01')
del f

assert read == b'\x01'
assert view == bytearray(b'\x01')

f = io.BufferedRandom(io.BytesIO(b'abcdefg'))
f.seek(3)
assert f.read(2) == b'de'
f.seek(4)
assert f.read(2) == b'fg'
f.seek(7)
assert f.read1(1) == b''

f = io.BufferedReader(io.BytesIO(b'abcdefg'))
assert f.read1(1) == b'a'
assert f.read1(1) == b'b'
assert f.read1(3) == b'cde'
assert f.read1(3) == b'fg'
assert f.read1(1
