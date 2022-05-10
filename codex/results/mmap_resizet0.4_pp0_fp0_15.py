import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code is supposed to read the first byte of the file and then truncate it.
However, it raises an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: memory mapping closed or invalid
</code>
If I remove the <code>f.truncate()</code> line, it works fine.
Why does this happen?
EDIT:
I'm using Python 3.4.3 on Windows 7.


A:

The problem is that <code>mmap</code> can't handle a file being truncated.  The documentation says:
<blockquote>
<p>The file size cannot be changed while mmap() is in use.</p>
</blockquote>
So if you truncate the file, the <code>mmap</code> object is invalid.

