import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that the <code>mmap</code> object is not updated when the file is truncated.
From the docs:
<blockquote>
<p>If the file on disk is resized by another process, the mmap object is
  adjusted to reflect the new size, and any new memory accesses are
  handled normally. If the file is resized smaller, the extra memory is
  freed, and any attempt to access it will raise a ValueError exception.</p>
</blockquote>
So, if you truncate the file, the <code>mmap</code> object is not updated, and you get the error.

