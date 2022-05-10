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
If I run this, I get a <code>NameError</code> because <code>view</code> is no longer defined.
If I change <code>view</code> to a global object, then the object is still there but the contents of the buffer are no longer there.
I can't find any documentation on this behavior.  Is this expected?  Is there a way to keep the buffer from being released?


A:

I see what you mean.  I think it's a bug.  The <code>readinto</code> method of <code>io.RawIOBase</code> calls <code>self._checkReadable</code>, which calls <code>self.readable()</code>.  But <code>self</code> is not <code>File</code>, it's <code>BufferedReader</code>, so <code>readable</code> is not <code>File.readable</code>, it's <code>BufferedReader.readable</code>, which returns <code>False</code>.  I think this is a bug.  It should call <code>self._raw.readable()</
