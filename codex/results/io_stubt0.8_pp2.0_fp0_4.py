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
print(len(view))
</code>
In Python 3, when <code>readinto()</code> is called in <code>BufferedReader.read()</code>, it's going to fill up the view and <code>del view</code> will destroy the buffer.  So, in Python 2, despite your first <code>del</code>, the second <code>del</code> will still crash, because <code>del buf</code> is called from <code>BufferedReader.__dealloc__()</code> and the <code>buf</code> is still referenced as <code>self._read_buf</code>.

