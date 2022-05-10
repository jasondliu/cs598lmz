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
print(bytes(view))
</code>
If you want to print the value of <code>view</code> after <code>File.readinto</code> was called, you need to use <code>io.RawIOBase.readinto</code> instead of <code>io.BufferedIOBase.readinto</code>. The latter doesn't store the buffer, but instead stores the result of <code>readinto</code> in <code>self._read_buf</code> and returns the number of bytes read.

