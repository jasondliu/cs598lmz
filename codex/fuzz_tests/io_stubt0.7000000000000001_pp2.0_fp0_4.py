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
del view # so we get a nice segfault instead of an Abort trap
</code>
That's pretty much where I got stuck, so I'm hoping someone with more familiarity with the io module can take it from here.

