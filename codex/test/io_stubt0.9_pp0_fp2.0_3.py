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
f = File()
len(view)
#Gets object into view so it's not deleted
f.readable()
del view
#Checks if finalization has occurred
