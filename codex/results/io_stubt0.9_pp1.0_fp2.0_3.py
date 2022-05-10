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
The reason I am trying to do this is so that I can use the buffered reader and writer classes to read and write portions of bytes from a file using an offset and size.


A:

No, currently buffered I/O implementations are always backed by some kind of file-like object.
Note that in Python (unlike C and C++), you can use <code>file()</code> (file streams) at the same time as <code>open()</code> (raw file descriptors).

