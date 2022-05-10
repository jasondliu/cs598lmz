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
sys.stdout.buffer.write(view)
</code>
<code>$ python3.5 /tmp/b.py
&lt;frozen importlib._bootstrap&gt;
</code>
I put the <code>del f</code> in there to make sure that the buffer was definitely destroyed.
This is pretty scary, because it means that even if you have an object and you're sure it doesn't have a reference to a buffer, it really might.
So I had a look through the source code for <code>BufferedReader</code> and <code>BufferedWriter</code> to see if I could find any other references to the buffer. The only thing I could find was the <code>_read_all_chunks</code> helper function, which keeps a list of chunks that it's read, each of which is a reference to the buffer.
So I tried the same trick with a <code>BufferedWriter</code>:
<code>import io

class File(io.RawIOBase):
    def write(self, buf):
        global view
        view = buf
    def writable(self
