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
view.tobytes()

# Check that it works with a BufferedRandom too

class File2(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def write(self, buf):
        pass
    def writable(self):
        return True

f = io.BufferedRandom(File2())
f.read(1)
del f
view.tobytes()

# Check that it works with a BufferedWriter too

class File3(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def write(self, buf):
        pass
    def readable(self):
        return True
    def writable(self):
        return True

f = io.BufferedWriter(File3())
f.read(1)
del f
view.tobytes()
