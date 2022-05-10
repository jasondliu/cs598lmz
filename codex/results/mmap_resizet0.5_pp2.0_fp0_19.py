import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this example, <code>a</code> is <code>b''</code>.
If I change the <code>m = mmap.mmap(f.fileno(), 0)</code> to <code>m = mmap.mmap(f.fileno(), 1)</code>, then <code>a</code> is <code>b'\x01'</code>.
I'm using Python 3.4.3 on Windows 7.


A:

<code>mmap</code> is a mapping from a file to memory.  When you truncate the file, you 'unmap' that memory.  You can't read from it anymore.

