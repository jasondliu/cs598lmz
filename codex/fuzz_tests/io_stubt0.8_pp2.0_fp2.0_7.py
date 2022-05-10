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
print(len(view)) # 1
del view

f = io.BufferedReader(File())
del f
try:
    view[0] = 1
    print("no error when accessing deallocated buffer")
except ReferenceError:
    print("ReferenceError when accessing deallocated buffer")

del view
