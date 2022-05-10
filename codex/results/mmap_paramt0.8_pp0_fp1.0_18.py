import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_WRITE)
    while True:
        print(m.size())
        m[0:1] = bytes(1)
        m.flush()
</code>
I want to increase the size of the file on disk when the program runs.
m.size() shows the size is increasing but the file size on disk doesn't increase, so I can't read the new bytes.


A:

<code>mmap.mmap</code> does not allocate or initialize memory that is outside of its initial size.
You can use <code>mmap.mmap.resize</code> to extend your <code>mmap</code> region.
There is no <code>mmap.mmap.resize</code> in Python 2.x, so you have to use <code>posix_fallocate</code> (if available) or <code>os.ftruncate</code> to increase the file size.
Example for Python 2.x:
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write
