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
This doesn't work:
<code>import io

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
The reason is that when <code>f</code> is deleted, the <code>BufferedReader</code> object is also deleted, which in turn deletes the <code>File</code> object. Since the <code>File</code> object is deleted, the <code>view</code> array gets deleted too.
This is not a problem in C because the <code>readinto</code> function is a C function and doesn't involve any reference counting.
The solution is to use <code>memoryview</code> instead of <code>bytearray</code>:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
       
