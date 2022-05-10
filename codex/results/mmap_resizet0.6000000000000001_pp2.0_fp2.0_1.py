import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In Python 2, this works fine, but in Python 3, I get an <code>IndexError</code> when trying to access a byte through the <code>[]</code> operator.
Why is this?


A:

This was a bug in Python that was fixed in Python 3.5. The bug report has more information.

