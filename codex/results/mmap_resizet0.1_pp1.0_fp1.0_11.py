import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file size is 0, but I don't understand why the offset is 1.
I'm using Python 3.6.1 on Windows 10.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap object is not updated if the underlying file is changed by other means. For example, if the file is truncated using ftruncate() while it is mapped in, the contents of the mapping will not be affected until a write is made to the mapped region.</p>
</blockquote>

