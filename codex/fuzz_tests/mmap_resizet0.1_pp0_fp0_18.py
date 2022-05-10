import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux, but on Windows it raises <code>ValueError: mmap offset is greater than file size</code>.
I'm not sure if this is a bug in Python or in Windows.
I'm using Python 3.6.5 on Windows 10.

