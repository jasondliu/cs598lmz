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
This is the error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    f.read(1)
  File "/usr/lib/python3.6/io.py", line 583, in read
    n = self._read_unlocked(n)
  File "/usr/lib/python3.6/io.py", line 643, in _read_unlocked
    n = self.raw.readinto(b)
  File "test.py", line 4, in readinto
    view = buf
ValueError: memoryview: underlying buffer is read-only
</code>
I've tried to use <code>memoryview(buf).cast("B")</code> but it doesn't work.
I've also tried to use <code>bytearray(buf)</code> but it doesn't work either.
I've tried to use <code>memoryview(bytearray(buf))</code> but it doesn't work either.
I've tried to use <code>memoryview
