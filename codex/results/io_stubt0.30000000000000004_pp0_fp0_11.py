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

print(view)
</code>
This prints <code>b'\x00'</code> on Python 3.4.3 and <code>b'\x00\x00'</code> on Python 3.5.1.
This is because <code>io.BufferedReader</code> uses <code>self._read_chunk()</code> to read data into the buffer.  On Python 3.4, <code>_read_chunk()</code> calls <code>self._raw_read()</code> which calls <code>self.raw.readinto()</code> with a <code>bytearray</code> of length <code>self.DEFAULT_BUFFER_SIZE</code>.  On Python 3.5, <code>_read_chunk()</code> calls <code>self._read_fast()</code> which calls <code>self.raw.readinto()</code> with a <code>memoryview</code> of length <code>self.DEFAULT_BUFFER_SIZE</code>.  In both cases, the length is <code>io.
