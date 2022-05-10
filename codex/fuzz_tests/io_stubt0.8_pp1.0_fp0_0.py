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

# This used to cause a segfault due to the error handling code in
# readinto() trying to use the view object after the associated File
# object had been deleted.
len(view)

# Try to reproduce http://bugs.python.org/issue12062
b = bytearray(range(256))

# The following line causes a segfault in the buffered readahead code
# in io.c. The cause is that the line:

#     self->readable = PyObject_GetAttrString(raw, "readable");

# returns NULL, but then none of the following checks for NULL are
# made:

#     if (!self->readable) {
#         PyErr_Clear();
#         self->readable = Py_True;
#         Py_INCREF(Py_True);
#     } else {
#         if (!PyCallable_Check(self->readable))
#             goto error;
#     }

# The final else clause calls the "readable" attribute, causing
# the segfault. The fix is to check that self->
