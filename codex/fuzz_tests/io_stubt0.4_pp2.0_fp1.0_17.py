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
The <code>io.BufferedReader</code> class is a wrapper around a file-like object that provides buffering.  It is a subclass of <code>io.RawIOBase</code>, which is an abstract base class for all raw I/O classes.  The <code>readinto</code> method is defined by <code>RawIOBase</code> as:
<blockquote>
<p>Read bytes into a writable buffer, returning the number of bytes read.
  The bytes are read from the underlying raw stream and into the
  writable buffer, which is then returned. None is returned when there
  is no more data to read. If the buffer is not writable, a TypeError
  is raised.</p>
</blockquote>
<code>io.BufferedReader</code> does not override <code>readinto</code>, so the default implementation is used.  The default implementation of <code>readinto</code> is to call the <code>read</code> method and copy the result into the buffer.  The <code>read</code> method is defined by
