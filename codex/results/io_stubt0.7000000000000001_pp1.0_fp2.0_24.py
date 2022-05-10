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
f = None
collect()
</code>
This program should cause a buffer overflow. It does not.
What is the correct way to do a buffer overflow in Python?

