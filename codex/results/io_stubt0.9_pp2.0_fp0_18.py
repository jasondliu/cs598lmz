import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f # required to close the file
print(view[0])     # expected to be 10 (ASCII newline)
</code>
However, this prints out <code>0</code> instead. Why does this happen?
I'm using Python 3.4 on Windows.


A:

The docs for <code>io.BufferedReader</code> are a bit cryptic, but I understand that "The buffer size is chosen using an informal heuristic: a larger buffer size is used for files on a network filesystem". So it might actually use an internal buffer that is bigger than <code>1</code>.

