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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I thought that the <code>mmap</code> object would be updated when the file is truncated.
I'm using Python 3.4.3 on Windows 7.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function is supported on Windows and Unix, and some other
  systems. On other systems, mmap() exists but only in an emulated form,
  where a normal file is used as a backing store.</p>
</blockquote>
So, on Windows, the <code>mmap</code> object is not updated when the file is truncated.

