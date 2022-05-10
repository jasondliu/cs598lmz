import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f  # or f.close()
del view  # or f.close()

gc.collect()
</code>
The whole program shows no sign of leaking memory.  The problem is that after <code>gc.collect()</code>, the Python interpreter still thinks the buffer is alive. I played around with other variations of the above example, and it seems like replacing <code>io.BufferedReader</code> with <code>io.BufferedRandom</code> prevents the leak.  I need a <code>BufferedReader</code>, though.

Another observation: if I create a "RawIOBase", it doesn't leak either; the problem seems to be specific to <code>BufferedReader</code>.


A:

This is a bug in the <code>io</code> module, see <code>io.c</code>:
<code>/* Create a new io object from a raw file descriptor, the
   raw file descriptor will be closed when the io object is destroyed.
   If closefd is false, the caller is responsible for closing the
   file descriptor. */
static PyObject *
PyIOBase_FD(int
