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

# check that a BufferedReader on a RawIOBase can be closed before the
# underlying RawIOBase

import io

class File(io.RawIOBase):
    def readable(self):
        return True

f = io.BufferedReader(File())
f.close()

# check that a BufferedReader on a RawIOBase can be closed after the
# underlying RawIOBase

import io

class File(io.RawIOBase):
    def readable(self):
        return True

f = io.BufferedReader(File())
f.detach()
f.close()

# check that a BufferedReader on a RawIOBase can be closed before the
# underlying RawIOBase

import io

class File(io.RawIOBase):
    def writable(self):
        return True

f = io.BufferedWriter(File())
f.close()

# check that a BufferedReader on a RawIOBase can be closed after the
# underlying RawIOBase

import io

class File(io.RawIOBase):
   
