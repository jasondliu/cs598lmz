import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I know that <code>mmap</code> is not a good solution for this problem, but I'm curious why this error is raised.


A:

The problem is that <code>mmap</code> is a view of the file, not a copy of it. So when you truncate the file, the <code>mmap</code> object is still pointing to the same place, but there is no data there.
If you want to truncate the file, you need to <code>close</code> the <code>mmap</code> object first.

