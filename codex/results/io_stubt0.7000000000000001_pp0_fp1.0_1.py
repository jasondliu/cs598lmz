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
del view

class File:
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
del view

class File:
    def readinto(self, buf):
        global view
        view = buf

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
del view

class File:
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File(), buffer_size=1024)
f.read(1)
del f
print(view)
del view

class File:
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File(), buffer_size=1024)
f.read
