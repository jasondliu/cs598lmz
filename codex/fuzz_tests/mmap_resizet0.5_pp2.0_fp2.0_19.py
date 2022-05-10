import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code produces an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
mmap.error: [Errno 22] Invalid argument
</code>
But if I comment out the <code>f.truncate()</code> line, it works.
Why does <code>f.truncate()</code> cause a problem?
I am using Python 3.6.2 on Windows 10.


A:

From the docs:
<blockquote>
<p>The file’s current position is not changed.</p>
</blockquote>
So, the mmap is still pointing to the same location in the file, and since you've truncated it, there is no data there.

