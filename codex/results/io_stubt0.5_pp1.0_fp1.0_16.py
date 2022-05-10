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
 
# io.BufferedReader.__init__ should not call the underlying file's
# readinto() method
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

class MyBufferedReader(io.BufferedReader):
    def __init__(self, file):
        super().__init__(file)

f = MyBufferedReader(File())
view = None
del f
view
 
# io.BufferedReader.__init__ should not call the underlying file's
# readinto() method
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

class MyBufferedReader(io.BufferedReader):
    def __init__(self, file):
        super().__init__(file)

f = MyBufferedReader(File())
view = None
f.close()
view

