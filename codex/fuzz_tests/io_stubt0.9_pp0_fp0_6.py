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
</code>
All of the above code is of course very simplified and I hope you get the picture. Another thing that comes to mind is concurrent reading and writing but maybe I just worry too much.

