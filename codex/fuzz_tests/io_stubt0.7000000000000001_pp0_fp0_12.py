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

import gc
gc.collect()

print(view[0])
</code>
The documentation states that
<blockquote>
<p>A file object is normally closed by explicitly calling its close() method. It is also closed when it is garbage-collected, but since garbage collection is non-deterministic, explicitly closing files is usually preferable.</p>
</blockquote>
but it seems that the file object is never closed.
I'm using Python 3.4.2 on Windows 7.


A:

This is because <code>io.BufferedReader</code> creates a new object that wraps around your <code>File</code> object and so that is going to be the object being collected.  That object's <code>__del__</code> is called, which calls <code>self.raw.close()</code>, which calls your <code>File</code>'s <code>close</code> method.  By default, that method does nothing.  The <code>File</code> object is not collected because it is referenced in your <code>view</code> array.
You can see this if
