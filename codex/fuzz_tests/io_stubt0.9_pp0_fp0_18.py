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
view
</code>
and got
<code>In [1]: run test.py
---------------------------------------------------------------------------
BufferError                              Traceback (most recent call last)
&lt;ipython-input-1-7631ed4b387d&gt; in &lt;module&gt;()
----&gt; 1 run test.py

c:\tmp\test.py in &lt;module&gt;()
     12     return True
     13 f = io.BufferedReader(File())
---&gt; 14 f.read(1)
     15 del f
     16 view

c:\python26\lib\io.pyc in read(self, n)
     45     def read(self, n=-1):
     46         buf = self._read(n)
---&gt; 47         self._read_buf = buf
     48         return buf
     49 

c:\python26\lib\io.pyc in _read(self, n)
    286         result = None
    287         if n is None or n &lt; 0:
--&gt; 288             result
