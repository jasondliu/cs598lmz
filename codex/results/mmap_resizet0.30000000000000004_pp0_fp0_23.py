import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get a <code>ValueError: mmap can't resize a read-only memory map</code> exception.
I'm using Python 3.3.3 on Linux.


A:

The problem is that you are opening the file in read-only mode.
<code>with open('test', 'r+b') as f:
</code>
should be
<code>with open('test', 'r+b') as f:
</code>

