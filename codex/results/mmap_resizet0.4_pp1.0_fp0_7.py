import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code fails with <code>ValueError: mmap offset is greater than file size</code> on the last line.
The problem is that the <code>mmap</code> object doesn't seem to know that the underlying file has been truncated.
I can work around this by calling <code>m.resize(0)</code> after the <code>f.truncate()</code>.
Is this the correct way to handle this situation?


A:

I think you should use <code>mmap.resize</code> to resize the mmap object.

