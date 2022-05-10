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
The <code>__del__</code> method of the <code>BufferedReader</code> object calls <code>self.raw.close()</code>, which calls <code>File.close</code>:
<code>def close(self):
    global view
    view[0] = 42
</code>
So it seems that Python is not attempting to run the <code>__del__</code> method of the <code>BufferedReader</code> object, but rather is attempting to run the <code>__del__</code> method of the <code>File</code> object.
If I replace <code>io.BufferedReader</code> with <code>io.TextIOWrapper</code> in the above example, I get the same behavior.
This doesn't make sense to me.  The <code>File</code> object is not being garbage collected, because the <code>BufferedReader</code> object still has a reference to it.  Why is Python attempting to run <code>File.__del__</code>?  Is this a bug in Python?


A:
