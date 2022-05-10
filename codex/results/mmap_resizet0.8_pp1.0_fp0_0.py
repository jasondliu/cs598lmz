import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It causes segmentation fault. This is probably because <code>truncate()</code> reduces the file size so the <code>m</code> is no longer valid.
How to overcome this problem? How to truncate a file so that the previous <code>mmap</code>ed data is not accessible?


A:

A <code>mmap</code> object is a mapping onto the file, not a copy of the data.  If the file is truncated, the <code>mmap</code> object tries to access the non-existent data and this causes the crash.
The problem with <code>truncate()</code> is that it cannot expand the file size either; this is an OS limitation.
To truncate the file, you have to call <code>close()</code> on the <code>mmap</code> object first.  Then the file can be truncated and recreated as a <code>mmap</code> object.

