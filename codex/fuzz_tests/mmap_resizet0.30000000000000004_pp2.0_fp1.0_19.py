import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
The error is clear, but I don't understand why the mmap is not updated when I truncate the file.
I'm using Python 3.6.5 on Linux.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is 0, the maximum length of the map is the current size of the file, except that if the file is empty the map must be zero length.</p>
</blockquote>
So, the <code>mmap</code> is not updated when you truncate the file, because you told it to be longer than the file.

