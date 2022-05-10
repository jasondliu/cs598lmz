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
In this example, the buffer object <code>view</code> is leaked. I know that the buffer object is not garbage collected because it is referenced from the <code>File</code> object as the <code>view</code> attribute. But that's not the point. In my real application, <code>f</code> is a wrapper around a TCP socket and the buffer object <code>view</code> is passed to a 3rd party library. I don't have access to the source of the 3rd party library, and it is not an option to modify it.
The question is: Is there any way to guarantee that the buffer object is garbage collected when the file object is deleted?
Edit: Of course, I know that it is possible to force the garbage collection by calling <code>gc.collect()</code>, but I'm looking for a solution that doesn't rely on this. The best solution would be a way to release the reference to the buffer object.

