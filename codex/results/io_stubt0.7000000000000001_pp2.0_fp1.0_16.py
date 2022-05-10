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

print(list(view))

print(list(view))
</code>


A:

You've hit a corner case. The <code>io</code> module is not intended for use with custom buffer types, and it doesn't support them at all.
You can see this in the source code for <code>PyBuffer_IsContiguous</code>, which is the function that determines whether or not the buffer is contiguous (and thus whether the <code>io</code> module can use it):
<code>static int
PyBuffer_IsContiguous(Py_buffer *view, char fort)
{
    char *ptr;
    Py_ssize_t sd;
    int k;

    if (view-&gt;suboffsets == NULL) {
        sd = 0;
        ptr = view-&gt;buf;
        for (k = 0; k &lt; view-&gt;ndim; k++) {
            Py_ssize_t stride = view-&gt;strides[k];
            Py_ssize_t shape = view-&gt;shape[k];

