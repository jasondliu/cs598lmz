import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError: mmap offset is greater than file size</code>.
I know that the mmap is invalidated when the file is truncated, but I would like to know how to get the data that was in the mmap before the truncate.
I'm using Python 3.4.4 on Linux.


A:

You can't.
The <code>mmap</code> object is a view into the file, and when you truncate the file, the view is no longer valid.
You can read the data before you truncate the file, but not after.

