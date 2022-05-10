import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I've tried with <code>m = mmap.mmap(f.fileno(), 1)</code> and <code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> but I get the same error.
I'm using Python 3.7.1 on Windows 10.


A:

You can't read from a <code>mmap</code> object after you truncate the file it's mapped to.
The Windows docs for <code>CreateFileMapping</code> say:
<blockquote>
<p>If the file is extended, the contents of the file between the old end of the file and the new end of the file are not guaranteed to be zero; the behavior is defined by the file system.</p>
</blockquote>
The docs for <code>
