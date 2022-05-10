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
The <code>CDataWrapper</code> type call into a C module that takes a pointer to a <code>PyObject</code> and store it in a <code>Py_buffer</code> structure. 
The C module is linked to Python via the def:
<code>PyObject* py_entry_point(PyObject *self, PyObject *args)
{
    PyObject *obj;
    if (!PyArg_ParseTuple(args, "O", &amp;obj))
        return NULL;

    Py_buffer buff;
    if (PyBuffer_IsContiguous(&amp;buff, 'C') == 1)
    {
         auto cdwd = PyObject_NEW(CDataWrapper, &amp;CDataWrapperType);
         cdwd-&gt;obj = obj;
         cdwd-&gt;buf = &amp;buff;
         Py_INCREF(obj);
         Py_XINCREF(buff.obj);
         return (PyObject*)cdwd;
    }

    PyErr_SetString(
