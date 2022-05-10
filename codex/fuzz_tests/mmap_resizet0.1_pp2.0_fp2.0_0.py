import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm using Python 3.6.1 on Windows 10.
I'm trying to understand why this is happening. I thought that the <code>mmap</code> object would be updated when the file is truncated.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. On
  Windows, it can only be used when mmap_mode is read-only; on Unix,
  mmap_mode can be read-write.</p>
</blockquote>
So, on Windows, the <code>mmap</code> object is read-only.

