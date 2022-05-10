import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>ValueError: cannot mmap an empty file</code>.
My question is where this check is in the mmap code. How Python is telling me that I called on an empty file. I tried changing the 0 to 1 but still I get this error. If I change the 1 to 100000 then it is executed with no problem. My expectation was that the OS would tell python that this file is empty.


A:

The error is raised in the <code>mmap.mmap()</code> constructor, when Python accesses the underlying system call, which itself returns an error through the Python C API.
See the very bottom of <code>Modules/mmapmodule.c</code>:
<code>static PyObject *
mmap_object(PyTypeObject *type, PyObject *args, PyObject *kwdict)
{
    Py_buffer map_view;
    PyObject *ret;
    mmap_object *m_obj;
    int fd;
    off_t offset;
    char *tag;
    Py_ssize_t length;  /* size of mmap,
