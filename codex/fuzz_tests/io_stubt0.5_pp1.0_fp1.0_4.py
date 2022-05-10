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
On CPython 3.7, the output is <code>b''</code>. The same is true for CPython 3.8, but on CPython 3.6, the output is <code>b'\x00'</code>.
The <code>gc.collect()</code> is needed because the buffer is only freed when the garbage collector runs, and it doesn't run automatically in the interactive interpreter.

