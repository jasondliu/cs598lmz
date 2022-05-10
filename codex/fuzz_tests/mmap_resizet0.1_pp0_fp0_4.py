import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws <code>ValueError: mmap offset is greater than file size</code> on the last line.
I understand that the file is truncated, but why does the mmap object still think that the file is 1 byte long?
I'm using Python 3.5.2 on Windows 10.


A:

The <code>mmap</code> object is not aware of the truncation. It is still mapped to the original file size.
You can use <code>mmap.resize</code> to resize the mapping:
<code>m.resize(0)
</code>

