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
print(view.obj)
print(view.obj.obj)
print(view.obj.obj.obj)
print(view.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj)
print(view.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj.obj)
print
