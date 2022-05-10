import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError: mmap offset is greater than file size</code>.
I'd like to understand why this happens. I expected <code>a</code> to be an empty <code>bytes</code> object.


A:

This is because the file descriptor of the file is still open, and the underlying file is truncated, but the mmap object is still pointing to the old file size.
You can see this by printing the <code>m.size()</code> before and after the <code>truncate()</code> call.

