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
</code>
In this case, <code>File.readable()</code> returns <code>True</code>, which <code>BufferedReader</code> calls in its <code>readinto()</code> implementation. When <code>readinto()</code> returns 0, the <code>BufferedReader.readinto()</code> method doesn't declare that the file is no longer <code>readable()</code> and then <code>readinto()</code> is called again and again. 
You can reproduce this using <code>io.open()</code>:
<code>def readinto(self, buf):
    return 0
def readable(self):
    return True

f = io.open("test.txt", "r", buffering=1024*1024, read_into=readinto)
f.readinto(bytearray(1024))    # endless loop
</code>
Note that this doesn't happen when <code>File.readinto()</code> throws an exception and <code>File.close()</code> is not called or when <code>readable()</code> returns <code
