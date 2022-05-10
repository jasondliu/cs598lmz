import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises:
<code>ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the mmap object is not updated.
I'm using Python 3.6.5 on Linux.


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. On
  Windows, it can only be used when mmap_mode is read-only, and
  Windows does not support the tagname and access arguments.</p>
</blockquote>
So it looks like <code>mmap</code> is not supported on Windows.

