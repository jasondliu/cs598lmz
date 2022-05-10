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
This works fine on Python 3.5.2, but fails on Python 2.7.9 with the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    f.read(1)
  File "/usr/lib/python2.7/io.py", line 1147, in read
    data = self._read1(n)
  File "/usr/lib/python2.7/io.py", line 1175, in _read1
    data = self._readinto(b)
  File "/usr/lib/python2.7/io.py", line 1143, in _readinto
    return self.readinto(buf)
  File "test.py", line 8, in readinto
    view = buf
TypeError: 'str' does not support the buffer interface
</code>
The error is caused by the fact that <code>view</code> is a <code>str</code> on Python 2 and a <code>memoryview</code>
