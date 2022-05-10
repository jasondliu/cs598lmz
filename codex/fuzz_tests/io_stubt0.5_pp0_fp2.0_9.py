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
print(view.base)
print(view.base is None)
</code>
The output is:
<code>&lt;memory at 0x7f3f3c3f2f00&gt;
&lt;memory at 0x7f3f3c3f2f00&gt;
False
</code>
I would expect the last line to be <code>True</code> because the object is being deleted. I'm using Python 3.6.3.

