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
del File
gc.collect()
print(view.tobytes())
</code>
This prints <code>b'\x00'</code>, and the <code>tobytes()</code> call can be replaced with <code>print(view)</code> to see the memory address of the <code>bytearray</code> object.

