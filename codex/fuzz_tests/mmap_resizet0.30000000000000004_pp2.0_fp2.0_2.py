import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I don't understand why.


A:

The <code>mmap</code> object is tied to the file descriptor.  It doesn't know anything about the file object.  When you truncate the file, the file descriptor is still pointing to the old file size.  The <code>mmap</code> object has no way to know that the file has been truncated.

