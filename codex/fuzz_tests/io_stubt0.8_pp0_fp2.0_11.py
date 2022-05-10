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

#test that read into view with offset and size
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.seek(1)
f.read(1)
del f
view

#test that read into view with offset and size
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view[0:5] = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.seek(1)
f.read(5)
del f
view

#test that read into view with offset and size
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view[0:5] = buf
    def readable(self):
        return True

f = io.BufferedReader(File())

