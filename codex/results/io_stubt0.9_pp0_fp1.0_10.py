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
print view
</code>
This program uses a <code>io.BufferedReader</code> to wrap a <code>File</code> object; the <code>File</code> object's <code>readinto</code> method assigns the argument given to it to a global variable. 
The <code>io.BufferedReader.read</code> method reads some data into its internal buffer and then calls <code>readinto</code> on that internal buffer, passing it <code>f.read(1)</code> causes it to read one byte into the <code>buf</code> argument and then assigns that very same buffer to <code>view</code>.
Note the <code>buf</code> is not copied; buffered readers when using <code>readinto</code> attempt to reduce system calls in order to improve performance.
Similar code is used from <code>urllib</code> to read into <code>buffer</code>s and <code>array</code>s, so I expect it is safe to assume that the <code>buf</code> given in <code>readinto</code> is not going to be
