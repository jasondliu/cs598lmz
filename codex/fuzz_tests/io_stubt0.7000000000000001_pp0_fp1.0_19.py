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
del File
</code>
The script will crash trying to access the deleted <code>File</code> instance.
I saw that <code>_io.BufferedReader</code> (in CPython) is implemented in C, so I dug a bit into the code and finally found the bug in <code>_io._decref_buffered</code>.
The problem is that the weakref callback is called after the object has already been freed, so <code>weakref.getweakrefcount</code> returns <code>0</code> and the <code>decref</code> function doesn't know that it must not decrement the refcount of the buffer. This causes <code>Py_DECREF</code> to be called on a freed object.
<code>void
_PyIO_decref_buffered(PyObject *obj)
{
    Py_ssize_t refcount;
    refcount = Py_REFCNT(obj);
    if (refcount == 1) {
        PyObject *buffer = ((PyBufferedReader *)obj)-&gt;raw;
        if (buffer != NULL)
           
