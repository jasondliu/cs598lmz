import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This code print <code>b'\x01'</code> as expected, but if I use <code>mmap.ACCESS_WRITE</code> flag:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>
It raises <code>ValueError: mmap can't enlarge file to larger than 0x7fffffff</code>
I'm using Python 3.6.6 on Ubuntu 18.04.
What is the reason for this?


A:

This is a known bug in the Python implementation of <code>mmap</code>. See https://bugs.python.org/issue21710.
It seems that the bug is only triggered when you read the <code>mmap</code> object with the <code>__getitem__</code> method.

