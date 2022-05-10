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
''.join(view)
</code>
which gives a local <code>view</code> to the string of interest, avoiding the creation of multiple copies, is as far as I can see not possible in Python given the current state of the buffering machinery. So the suggestion to clone <code>buf</code> before operating on it, is the usual and recommended way to deal. This is suggested in the more recent <code>io</code> docs; and in the Documentation/source even since Python 2.3, contrary to what the other answers and comments claim.
Even a <code>io.TextIOBase</code> implementation cannot avoid this, because <code>TextIOBase.read()</code> will have to read the raw data, too. The only possibility I see would be a non-buffered file-like object implementing <code>io.TextIOBase</code>, whose <code>read(n)</code> method would read the underlying text, decode it, and only return the up-to-n bytes of it. 

