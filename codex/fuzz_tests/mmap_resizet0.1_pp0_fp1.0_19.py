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
ValueError: mmap offset is greater than file size
</code>
I would expect the <code>mmap</code> to be updated when the file is truncated. Is there a way to do this?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. On
  Windows, it can only be used when mmap_mode is read-only; on Unix,
  mmap_mode can be read-write, but this is not guaranteed to work on all
  Unix flavors.</p>
</blockquote>
So, you can't use <code>mmap</code> to truncate a file.

