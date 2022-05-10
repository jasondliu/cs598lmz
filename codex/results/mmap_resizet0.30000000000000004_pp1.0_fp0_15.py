import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
I would expect that the <code>m</code> object is still valid after the <code>truncate</code> call.
Is this a bug or am I doing something wrong?


A:

The documentation for <code>mmap</code> states:
<blockquote>
<p>The file must be opened in a mode that supports reading and writing. The mmap() function is available in the mmap (or mmapmodule) module.</p>
</blockquote>
I think you are confusing the file mode with the <code>mmap</code> mode.  The file needs to be opened in a mode that supports reading and writing.  The <code>mmap</code> mode should be <code>mmap.ACCESS_WRITE</code>.
<code>import mmap

with open('test
