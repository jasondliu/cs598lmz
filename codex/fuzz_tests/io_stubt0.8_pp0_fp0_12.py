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
if run.dis(view, 1) != "POP_TOP":
    raise Exception
</code>

If <code>py_buffered_read</code> can be made to return a reference to the internal buffer (any reference should do, but the strongest one possible is optimal), you could use the reference to store the buffer in a global variable or pass it to another function and then return without touching the object.
If <code>py_buffered_read</code> can be made to return <code>NULL</code>, it will just return <code>NULL</code> without touching the object.
If <code>py_buffered_read</code> can be made to return an arbitrary pointer, it can be used to overwrite the type pointer, in which case no GC is performed on the object at all.
Otherwise, if <code>py_buffered_read</code> can be made to return <code>0</code>, CPython will try to decref the buffer object, which will decrement its reference count to -1, which will cause the object to be collected during the next collection pass, and an arbitrary Python object can
