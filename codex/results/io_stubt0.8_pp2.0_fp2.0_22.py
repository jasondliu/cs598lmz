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
f = io.BufferedReader(File())
f.read(1)
f.read(1)
</code>
It crashes when <code>f.read(1)</code> is called on the second <code>BufferedReader</code>.


A:

I think I've found the error. It's not in the <code>BufferedReader</code> class, but in the <code>fileio</code> module. More specifically, this part is relevant:
<code>if (Py_TYPE(self)-&gt;tp_flags &amp; Py_TPFLAGS_HAVE_NEWBUFFER) {
    Py_buffer view;
    if (!_PyIO_get_view(self, &amp;view, PyBUF_WRITABLE))
        return NULL;
    err = PyBuffer_Release(&amp;view);
    if (err)
        return NULL;
}
</code>
This is called when a <code>BufferedWriter</code> or <code>BufferedRandom</code> is created. It holds a reference to the buffer view - and since I don't
