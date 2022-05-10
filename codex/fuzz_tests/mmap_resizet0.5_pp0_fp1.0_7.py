import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises an error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
The error goes away if I remove the <code>f.truncate()</code> line.
I'm using Python 3.6.2 on Ubuntu 16.04.


A:

This is a bug in Python 3.6.2, which was fixed in Python 3.6.3.

