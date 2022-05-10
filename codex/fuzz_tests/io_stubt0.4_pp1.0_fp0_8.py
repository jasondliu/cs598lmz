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
This code gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    f.read(1)
  File "/usr/lib/python3.2/io.py", line 643, in read
    data = self._read1(n)
  File "/usr/lib/python3.2/io.py", line 693, in _read1
    return self.raw.readinto(b)
AttributeError: 'File' object has no attribute 'raw'
</code>
This is because the <code>BufferedReader</code> object is not calling the <code>readinto</code> method of the <code>File</code> object, but instead is calling the <code>readinto</code> method of the <code>File</code> object's <code>raw</code> attribute.  However, the <code>File</code> object doesn't have a <code>raw</code> attribute.
I have found that if I change the <code>File</code>
