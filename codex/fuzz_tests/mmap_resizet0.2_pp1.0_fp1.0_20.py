import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws <code>ValueError: mmap closed or invalid</code>.
I'm not sure if this is a bug or not, but it seems like it should be possible to read from a mmap after truncating the underlying file.
I'm using Python 3.5.2 on Windows 10.


A:

This is a bug in the Windows implementation of <code>mmap</code>.
The problem is that the <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is created with a size of 1, but the file is truncated to 0.
The <code>mmap</code> object is not updated, so it still thinks the file is 1 byte long.
When you try to read from the <code>mmap</code> object, it tries to read from the file at offset 1, which is past the end of the file.
This causes the <code>ValueError</code> exception.
The <code>mmap</code> object should be updated when the file is truncated.
This is a
