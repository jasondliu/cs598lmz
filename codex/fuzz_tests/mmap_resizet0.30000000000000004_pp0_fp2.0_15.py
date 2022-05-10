import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would have expected that the <code>mmap</code> object would be updated to reflect the new file size.
I'm using Python 3.6.5 on Ubuntu 18.04.


A:

This is a known bug in Python 3.6 and earlier. It is fixed in Python 3.7.

