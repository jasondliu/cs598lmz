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
gc.collect()
view
</code>
<blockquote>
<p>'\x00'</p>
</blockquote>
So here, <code>io.BufferedReader</code> doesn't free the <code>PyObject</code> representing the <code>File</code> instance <code>f</code> if the buffer it uses is a Python object.
If it gets created by allocating a buffer of one byte and increasing it, all is fine.
If I change the buffer creation code (in <code>PyBuffer_FromObject</code>) to use a memoryview like that, then the memoryview is kept too, so the test case passes.
But this is not a viable solution because I would have to grab the reference to the memoryview, which would make the instance of my class not hashable (or would only make it hashable if the memoryview can be used as a hash key).
I'm probably missing something obvious, but I could not find any other option.
So the question is: how can I implement a custom buffer for Python 3 or 2 in Cython and still make my class hashable?


A:


