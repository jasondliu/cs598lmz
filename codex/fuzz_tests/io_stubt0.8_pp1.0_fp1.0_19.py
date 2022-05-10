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

view[0] = 47
"""
    stdout = run(code)
    assert stdout == b"/"

def test_readinto_truncate():
    code = b"""\
import io

class File(io.RawIOBase):
    def __init__(self):
        self.data = b"foo"

    def readinto(self, buf):
        global view
        view = buf[:len(self.data)]
        view[:] = self.data
        return len(self.data)

    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

view[0] = 47
view[1:] = b"oo"
"""
    stdout = run(code)
    assert stdout == b"/foo"

def test_readinto_too_big():
    # Reads that are larger than the buffer size return only the actual data
    # that was read into the buffer
    code = b"""\
import io

data = b"foo"

