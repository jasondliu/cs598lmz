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
gc.collect()
view
f = io.BufferedReader(File())
f.read(1)
f.close()
f = io.BufferedReader(File())
f.read(1)
f.closed
f.fileno()
f.close()

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
f = io.BufferedReader(File(), buffer_size=0)
f.peek(1)
view
f.peek(1)
view
f.close()

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
f = io.BufferedReader(File(), buffer_size=1)
f.peek(1)
view
f.peek(1)
view
f.peek(2)
view
f.close()

class File(io.RawIOBase):
    def readinto
