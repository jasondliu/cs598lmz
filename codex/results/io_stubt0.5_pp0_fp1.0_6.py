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

view[0] = 1
</code>
The idea is to use the buffer of the <code>io.BufferedReader</code> as a view into the <code>memoryview</code> of the <code>bytearray</code> that was passed to <code>io.BufferedReader</code>. The problem is that the <code>io.BufferedReader</code> buffer is not exposed, so I can't get a <code>memoryview</code> of it.
Is there a way to get a <code>memoryview</code> of the buffer of a <code>io.BufferedReader</code>?

