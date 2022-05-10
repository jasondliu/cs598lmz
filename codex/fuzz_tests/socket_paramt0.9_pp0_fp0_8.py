import socket
socket.if_indextoname(17)

Output
lo0
</code>
Is there any way to get the interface name in c using Python header files or using any c header files.
Thanks in advance.


A:

<code>#include &lt;Python.h&gt;
#include &lt;structmember.h&gt;

static PyObject *
_if_indextoname(PyObject *self, PyObject *args)
{
    int index;
    char if_name[_MAX_INTERFACES_NAME_LENGTH];
    if (!PyArg_ParseTuple(args, "i", &amp;index))
        return NULL;
    if (if_indextoname(index, if_name) == NULL)
    {
        return PyErr_SetFromErrno(PyExc_OSError);
    }
    return PyUnicode_FromString(if_name);
}

static PyMethodDef If_Methods[] = {
    {"if_indextoname",  _if_indextoname, METH_VARARGS,
     "
