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
</code>
This code produces a <code>cannot import name File</code> error. However, if I change <code>File</code> to <code>Foo</code> or <code>Bar</code>, the code runs as expected (i.e. I get a <code>TypeError: 'NoneType' object is not callable</code> when I try to read from <code>f</code>).
Why does <code>io.BufferedReader</code> behave differently when the class name is <code>File</code>?


A:

This is a bug in <code>io.py</code>.
When <code>io.py</code> was first written, it looked something like this:
<code>import _io

class FileIO(_io._FileIO):
    def __init__(self, file, mode='r', closefd=True):
        _io._FileIO.__init__(self, file, mode, closefd)
    def readable(self):
        return True
</code>
Then, the C code was changed to work with Python
