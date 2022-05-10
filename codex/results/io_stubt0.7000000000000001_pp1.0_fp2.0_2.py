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
f = File()
f.readinto(view)
</code>
If you don't want to subclass <code>io.RawIOBase</code>, you can also use <code>io.open()</code> to create the file object
<code>f = io.open(0, 'rb', buffering=0)
f.readinto(view)
</code>
The <code>io.BufferedReader</code> constructor also accepts a <code>buffer_size</code> parameter for the buffer size (defaults to <code>DEFAULT_BUFFER_SIZE</code>), and a <code>max_buffer_size</code> parameter for the maximum buffer size (defaults to <code>io.DEFAULT_BUFFER_SIZE</code>).

