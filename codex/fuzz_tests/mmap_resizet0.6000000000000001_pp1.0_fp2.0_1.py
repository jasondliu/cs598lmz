import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
However, if I change <code>f.write(bytes(1))</code> to <code>f.write(bytes(2))</code> then <code>a</code> is <code>b'\x00'</code>.
In Python 3.3, it behaves as I expected in both cases.
What is happening here?


A:

This is a known bug in Python 2.7.
It was fixed in Python 3.2.

