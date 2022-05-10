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
    def write(self, buf):
        global view
        view = buf
    def writable(self):
        return True

f = io.BufferedWriter(File())
f.write(b"hello")
del f
view

import pickle
import io

class File(io.RawIOBase):
    def write(self, buf):
        global view
        view = buf
    def writable(self):
        return True

f = io.BufferedWriter(File())
pickle.dump(b"hello", f)
del f
view

import pickle
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
