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
gc.collect()

print(view)
</code>
<blockquote>
<p>Traceback (most recent call last):   File
  "/usr/lib/python3.2/io.py", line 1236, in _get_decoder
      return self._decoder or locale.getpreferredencoding() AttributeError: 'NoneType' object has no attribute 'getpreferredencoding'</p>
</blockquote>
It seems that <code>BufferedReader</code> is trying to set the decoder after the <code>File</code> object has been destroyed, which is not allowed.

