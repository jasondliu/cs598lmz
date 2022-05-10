import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # crash
</code>
The crash happens in <code>mmap_find()</code> in the following code:
<code>Py_ssize_t
mmap_find(mmap_object *self, PyObject *args)
{
   ...
   if (!PyString_Check(arg) || !(string = PyString_AS_STRING(arg))) {
       PyErr_SetString(PyExc_TypeError, "need a character buffer object");
       return -1;
   }
   ...
}
</code>
<code>arg</code> is <code>NULL</code> here.
My environment: Python 2.7.3, Windows 7 64-bit.


A:

You can not use <code>mmap</code> anymore after truncating the file. Even if it would have worked, the new contents of the file would have been the contents of the original file starting from the current cursor position.

