import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think that the problem is that <code>truncate</code> doesn't change the file size in the file descriptor, but I don't know how to fix it.


A:

The problem is that <code>mmap</code> uses the file size from the file descriptor, not from the file itself.
The solution is to use <code>mmap.resize</code> instead of <code>truncate</code>.

