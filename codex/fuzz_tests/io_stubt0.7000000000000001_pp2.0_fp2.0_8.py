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

if view is not None:
    print("test failed")
</code>
The test succeeds (no output printed) with <code>python2.7</code> and <code>python3.3</code>, fails (with "test failed" printed) with <code>pypy 2.0.2</code> and <code>python3.1</code>.
The documentation doesn't mention anything about this behaviour. Is this a bug in python or in PyPy or am I missing something?
If this is a bug, where should I report it?


A:

<blockquote>
<p>The documentation doesn't mention anything about this behaviour.</p>
</blockquote>
The <code>file</code> docs do provide some specification of the behaviour you're seeing:
<blockquote>
<p>The <code>&lt;code&gt;file&lt;/code&gt;</code> object provides a set of I/O methods that can be used to read and write a file.</p>
</blockquote>
Now, you're not passing a <code>file</code> object, but a
