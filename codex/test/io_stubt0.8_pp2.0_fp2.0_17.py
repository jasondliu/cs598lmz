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


def test_buf():
    global view
    view[0] = ord('a')
    view[1] = ord('b')
    view[2] = ord('c')
    view[3] = ord('d')
    return view


def target(*args):
    return test_buf, args
