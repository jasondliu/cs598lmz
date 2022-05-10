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

def callback(buf):
    global size
    size = len(buf)

def main():
    global size
    size = None
    buf = bytearray(b"abc")
    callback(buf)
    assert size == 3
    buf = bytearray(b"abc")
    callback(memoryview(buf))
    assert size == 3
    buf = bytearray(b"abc")
    callback(memoryview(buf)[1:])
    assert size == 2
    buf = bytearray(b"abc")
    callback(memoryview(buf)[1:3])
    assert size == 2
    buf = bytearray(b"abc")
    callback(memoryview(buf)[1:3:2])
    assert size == 1
    buf = bytearray(b"abc")
    callback(memoryview(buf)[1:3:2])
    assert size == 1
    buf = bytearray(b"abc")
    callback(memoryview(buf)[1:3:2])
    assert size == 1
