import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f, File

class NewFile(io.RawIOBase):
    def readinto(self, buf):
        # buf[:] = b""
        buf[:] = b"123456789"
    def readable(self):
        return True

f = io.BufferedReader(NewFile())
print(f.read(1))
</code>
Everything works fine, the b"123456789" is written into the buffer, and the print statement prints b"1". But the problem is that if I don't write anything into the buffer, I have a segmentation fault.
It seems that readinto requires the buffer being overwritten. I was wondering if there is a way to make readinto not overwrite the buffer.

