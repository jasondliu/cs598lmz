import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
In Python 2, it works as I expected, but in Python 3 the output is <code>b'\x00'</code>.
In Python 3, it seems that the <code>mmap</code> object does not update its size when <code>truncate</code> is called.
Is there a way to make <code>mmap</code> update its size when the underlying file is truncated?

