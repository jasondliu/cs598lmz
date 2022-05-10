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
print(view)
</code>
This prints <code>b'\x00'</code> on my machine, which is the first byte of the <code>bytearray</code> that was allocated by the <code>io</code> module.

