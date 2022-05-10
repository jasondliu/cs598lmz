import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux, but on Windows it raises <code>ValueError: mmap offset is greater than file size</code>.
I'm using Python 3.6.5 on Windows 10.
Is this a bug or am I doing something wrong?


A:

I think this is a bug in the Windows implementation of <code>mmap</code>.
I've filed a bug report on the Python bug tracker.

