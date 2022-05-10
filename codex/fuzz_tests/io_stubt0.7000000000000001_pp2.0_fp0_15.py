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
The above code produces a warning:
<code>/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gc.py:352: 
RuntimeWarning: tp_compare didn't return -1 or -2 for exception
if lineno &gt;= 0:
</code>
It doesn't matter which OSX version you use, the warning shows up on all of them.
Given that I'm using the C API to create my buffer, is there a way to get rid of the warning?
The code to create the buffer is as follows:
<code>PyObject *PyBuffer_FromReadWriteMemory(void *ptr, Py_ssize_t size)
{
    return PyBuffer_FromMemory(ptr, size);
}

PyObject *PyBuffer_FromReadWriteObject(PyObject *base, Py_ssize_t offset, Py_ssize_t size)
{
    return PyBuffer_FromObject(base, offset, size);
}
</code>

