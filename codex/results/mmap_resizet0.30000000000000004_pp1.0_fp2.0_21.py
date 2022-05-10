import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError</code> on the last line.
<code>ValueError: mmap length is zero
</code>
I understand that the <code>mmap</code> object is no longer valid after the <code>truncate</code> call, but I don't understand why I can't just read from it.
I'm using Python 3.5.2 on Ubuntu 16.04.


A:

The <code>mmap</code> object is still valid, but the underlying file has been truncated, so there is no data to read.

