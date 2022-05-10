import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
The file <code>test</code> is not changed.
What am I doing wrong?


A:

The problem was that Python 2.7.11 on Windows does not support <code>mmap.ACCESS_WRITE</code> (see <code>mmap.py</code>).

