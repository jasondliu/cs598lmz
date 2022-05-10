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
This code works fine, but I wonder if it is possible to use a <code>io.BufferedReader</code> without creating a new class.
I tried using <code>io.BytesIO</code> instead of <code>File</code>, but it doesn't work.
<code>import io

f = io.BufferedReader(io.BytesIO(b'a'))
f.read(1)
del f

print(view)
</code>
This code doesn't work because <code>BytesIO</code> doesn't have a <code>readinto</code> method.
Is it possible to use <code>io.BufferedReader</code> without creating a new class?


A:

You can use <code>io.BytesIO</code> as the base class for your <code>File</code> class.
<code>import io

class File(io.BytesIO):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io
