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

view.release()
try:
    view.release()
except ValueError:
    pass
else:
    print("FAIL: expected a ValueError")

def test_readinto():
    global view2
    f = io.BufferedReader(File())
    f.read(1)
    view2 = memoryview(f)
    del f
    view2.release()
    try:
        view2.release()
    except ValueError:
        pass
    else:
        print("FAIL: expected a ValueError")
