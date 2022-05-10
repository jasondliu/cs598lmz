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
view[0] = 42
</code>
If the interpreter has not yet garbage collected f, the final line will cause a segfault because the memory the <code>BufferedReader</code> object refers to will be invalid (it will have been free'd by the <code>BufferedReader.__del__</code> method).  If the interpreter has already GC'd f, the program should exit normally.  If you run it with <code>--debug</code> and get no GC messages, you know it's happened already.
(The Python 2.7.11 <code>BufferedReader.__del__</code> method looks like this:
<code>static void
bufferedreader_dealloc(PyBufferedReaderObject *self)
{
    Py_CLEAR(self-&gt;raw);
    Py_TYPE(self)-&gt;tp_free((PyObject *)self);
}
</code>
where <code>Py_CLEAR</code> is a macro expanding to:
<code>#define Py_CLEAR(op)                        \
        do {                                \
                if (op)
