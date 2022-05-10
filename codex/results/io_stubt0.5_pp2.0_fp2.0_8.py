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
This raises a <code>ValueError: I/O operation on closed file</code> because the <code>BufferedReader</code> is closed when the <code>File</code> object is deleted.  I can't find anything in the documentation that says that an <code>io.BufferedReader</code> object can't be used as a context manager, so I'm wondering if this is a bug or if I'm missing something.  I can't find any examples where a <code>BufferedReader</code> is used as a context manager, so I'm guessing it's not supposed to be used that way.


A:

<code>io.BufferedReader</code> is a <code>io.BufferedIOBase</code> subclass, and <code>io.BufferedIOBase</code> is not a context manager.  This is documented:
<blockquote>
<p><strong>class <code>&lt;code&gt;io.BufferedIOBase&lt;/code&gt;</code></strong></p>
<p>Base class for buffered IO objects.
  <strong
