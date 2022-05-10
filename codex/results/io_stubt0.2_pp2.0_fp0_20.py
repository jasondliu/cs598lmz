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

# io.BufferedReader.readinto() calls io.RawIOBase.readinto()
# which calls io.RawIOBase.read()
# which calls io.BufferedReader.read()
# which calls io.BufferedReader.read1()
# which calls io.BufferedReader.readinto1()
# which calls io.RawIOBase.readinto()
# which calls io.RawIOBase.read()
# which calls io.BufferedReader.read()
# which calls io.BufferedReader.read1()
# which calls io.BufferedReader.readinto1()
# which calls io.RawIOBase.readinto()
# which calls io.RawIOBase.read()
# which calls io.BufferedReader.read()
# which calls io.BufferedReader.read1()
# which calls io.BufferedReader.readinto1()
# which calls io.RawIOBase.readinto()
# which calls io.RawIOBase.read()
# which calls io.BufferedReader.read()
# which calls io.BufferedReader.read
