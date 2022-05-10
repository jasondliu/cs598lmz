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
This prints <code>None</code> on Python 2 and <code>b''</code> on Python 3.

What's the difference between the two implementations?
Is there anything I can do to make the Python 2 version work the same as the Python 3 version (without changing the <code>File</code> class)?



A:

The difference is that in Python 2, the <code>f</code> object is not garbage collected when you delete it.
<code>from io import BytesIO
from sys import version_info

def read_one(f):
    f.read(1)

def test():
    f = BytesIO()
    read_one(f)
    del f

test()

if version_info[0] == 2:
    import gc
    gc.collect()
</code>
In Python 2, the <code>gc.collect()</code> at the end shows that <code>f</code> is still alive, and the <code>f.readinto()</code> method is still called after <
