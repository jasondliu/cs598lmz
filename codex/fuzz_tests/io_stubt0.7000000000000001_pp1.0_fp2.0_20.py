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

view[0] = ord('a')
</code>
But is there a more idiomatic way to do this?  Something like <code>foo = bytearray(file(...))</code>?
I don't want to use <code>file(...).read()</code> because that would read the entire file into memory.


A:

If you're looking for a way to create a <code>bytearray</code> directly, then you can use <code>bytearray.fromfile</code>:
<code>data = bytearray.fromfile(file)
</code>
In general you should be aware that the <code>file</code> object is a legacy name for the <code>io.FileIO</code> class, which is a direct subclass of <code>io.RawIOBase</code>, and the <code>io</code> module is the standard way to handle binary I/O in Python.

