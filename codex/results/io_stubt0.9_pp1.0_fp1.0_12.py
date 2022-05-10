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
And the results:
<code>&gt;&gt;&gt; import test
&gt;&gt;&gt; for i in range(5):          # Counting references.
...     del test.view[0]
... 
&gt;&gt;&gt; test.view
b''  # &lt;----------------------- Final "del" succeeded.
</code>
Thus, references to the buffer are released and the <code>del</code> can succeed, but one of the references is held by a Python object that you cannot get to. It's inside the <code>BufferedReader</code> object (and we can check exactly where, as described here).
The long term solution is to not use <code>io</code> objects as a means to access memory buffers. Use the Python <code>mmap</code> module, or a combination of <code>ctypes</code> and objects from the <code>ctypes</code> extension modules, or objects from the <code>_ctypes</code> C API. One can also use the <code>array
