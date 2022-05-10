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
</code>
Live Demo
I was thinking that perhaps the <code>BufferedReader</code> object was keeping a reference to the underlying <code>File</code> object (and therefore the byte buffer) even after the reader was closed, but I confirmed in this example that <code>File</code> objects are collected when no longer referenced.
So how do we make sure that the buffer is eligible for garbage collection?


A:

You can't. The code will retain a reference to the buffer until the <code>io.BufferedReader</code> is garbage collected, and there is no way to speed that up.
In your example, the <code>f</code> reference will be removed immediately after the <code>f.read(1)</code> line completes, exactly at the same time, but before the <code>del f</code> line executes.
This might be a minor leak; if you keep creating and discarding <code>io.BufferedReader</code> instances, then the first block allocated for each instance is not released until the <code>BufferedReader</code> itself is garbage collected. While this memory is
