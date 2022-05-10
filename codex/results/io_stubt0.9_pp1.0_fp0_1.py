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

def f():
    global seen
    seen = set()
    view.append(1)
    view.extend([2])

f()
print(view, seen)
del view, seen
