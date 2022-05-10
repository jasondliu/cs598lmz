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
view
 
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.seek(1,2)
del f
 
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def writable(self):
        return True
    def truncate(self, size=-1):
        return 0

f = io.BufferedWriter(File())
f.write("a")
del f
view
 
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def writable(self):
        return True
    def truncate(self, size=-1):
        return 0

f = io.BufferedWriter(File())
f.truncate(10)
del f
 
class File(io.RawIOBase):
    def readinto(self, buf
