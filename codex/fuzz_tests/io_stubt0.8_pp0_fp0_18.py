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

def read(self):
    return view[0]

def readinto(self, buf):
    buf[:] = view[:len(buf)]
    return len(buf)
    
io.BufferedReader.readinto = readinto
io.BufferedReader.read = read

import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.readinto(b"")
del f

def read(self):
    return view[0]

def readinto(self, buf):
    buf[:] = view[:len(buf)]
    return len(buf)

io.BufferedReader.readinto = readinto
io.BufferedReader.read = read

import io

class File(io.RawIOBase):
    def write(self, buf):
        global view
        view = buf
    def writable(self):
        return True

f = io.
