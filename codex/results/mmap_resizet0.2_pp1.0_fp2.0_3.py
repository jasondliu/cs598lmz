import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives me a <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated, but why does the mmap object still think that the file is 1 byte long?
I'm using Python 3.4.


A:

The <code>mmap</code> object is not aware of the file size. It is just a view of the file.
The <code>mmap</code> object is created with a size of 0. This means that it is a view of the whole file.
When you truncate the file, the <code>mmap</code> object is still a view of the whole file.
When you try to access the <code>mmap</code> object, it tries to access the whole file, but the file is empty, so it raises an exception.

