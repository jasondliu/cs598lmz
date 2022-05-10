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

if sys.version_info.major &lt; 3:
    import ctypes
    ctypes.cast(id(view), ctypes.c_void_p).value = 0
del view
</code>
But neither works when <code>view</code> is deleted.
Relevant question, but does not cover the case when Python (CPython) is shutting down.


A:

I thought about this for about ten minutes, and the conclusion I came to, is that if the object is being deleted after the interpreter shutdown, then you don't need to delete it.
If the interpreter is done, nothing will ever use your object again, not even the object finalizer.
If you do not want your object to hang around until all memory is reclaimed, then you should not set the <code>__del__</code> method.  In fact, there is evidence that you shouldn't do this.  It's a huge pain.
If the object is still live after the interpreter shuts down, then you have a memory leak.

