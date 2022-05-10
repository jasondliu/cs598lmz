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

print(view)
</code>
Output (CPython):
<code>bytearray(b'\x00')
</code>
Output (PyPy):
<code>bytearray(b'')
</code>
It seems that PyPy is doing a <code>memmove</code> instead of a <code>memcpy</code> in <code>pypy_b_readinto_wbuf_wlen</code> (in <code>cpyext/buffered.c</code>):
<code>  if (PyObject_AsWriteBuffer(w_view, (void **)&amp;p, &amp;len_) &lt; 0) {
    PyBuffer_Release(&amp;buf);
    return NULL;
  }
  if (len_ &lt; length)
    length = len_;
  memmove(p, buf.buf, length);
</code>
Is PyPy's behavior correct? It seems that this behavior is creating incorrect assumptions (e.g. in <code>pypy/module/cpyext/test/
