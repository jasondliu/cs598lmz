import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code works on Linux, but not on Windows. On Windows, it raises <code>ValueError: mmap offset is greater than file size</code>.
I'm not sure if this is a bug in Python or Windows, but I'd like to know if there is a workaround.


A:

The problem is that the <code>mmap</code> object is not aware that the file has been truncated.  You can fix this by calling <code>m.resize(0)</code> before reading from the <code>mmap</code> object.

