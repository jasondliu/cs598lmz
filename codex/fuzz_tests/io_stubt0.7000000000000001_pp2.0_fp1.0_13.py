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
I get an error, <code>NameError: global name 'view' is not defined</code>. Why is that?


A:

<code>File</code> doesn't inherit from <code>io.RawIOBase</code>, so you need to define <code>readable</code> yourself:
<code>class File(object):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
</code>

