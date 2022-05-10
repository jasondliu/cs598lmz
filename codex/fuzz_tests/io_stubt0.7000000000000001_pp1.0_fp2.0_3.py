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
view.release()

view = mmap.mmap(-1, 1, tagname='pymap')
f = io.BufferedReader(File())
f.read(1)
del f
view.release()
