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
# memoryview still has reference to underlying buffer
</code>
Apparently, I could keep a reference to <code>f</code> or just call <code>f.read()</code> without <code>int</code> instead, but I would like to know how to avoid such a situation. Does the standard library provide a way to handle this? Or what is the most Pythonic way of working around this issue?


A:

You could use <code>bytearray</code> and update it in-place with <code>memoryview.cast</code>.
<code>b = bytearray(1)
m = memoryview(b)

(...)
f.readinto(m.cast('B'))
</code>

