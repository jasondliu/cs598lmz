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
</code>
I forgot to call <code>gc.collect</code> in the end of the code. The <code>gc</code> module acts like a boss.

