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
This works for 3.4.2, 3.5.1, 3.6.0, 3.7.0, and 3.8.0, but not for 3.7.1, 3.7.2, or 3.8.1.  Is there a new way to do what I'm trying to do or is this an actual bug?


A:

It's a change in the reference count of the <code>int</code> object <code>1</code>.
In Python 3.7.1, this is the C code for the <code>f.read(1)</code> call:
<code>{
        Py_ssize_t k;
        PyObject *sizeobj;

        sizeobj = PyLong_FromSsize_t(n);
        if (sizeobj == NULL) {
            Py_DECREF(method);
            return NULL;
        }
        args = PyTuple_Pack(1, sizeobj);
        Py_DECREF(sizeobj);
        if (args == NULL) {
            Py_DECREF(method);
            return NULL
