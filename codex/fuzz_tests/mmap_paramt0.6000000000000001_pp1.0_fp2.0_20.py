import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    m[0] = bytes(2)
</code>
I would like to write a byte array to a particular position in a file, without overwriting the rest of the file.
However, the following error is thrown:
<code>TypeError: must be convertible to a buffer, not int
</code>
I am using Python 3.6.2.


A:

You can do it like this:
<code>m = mmap.mmap(f.fileno(), 0)
m[0] = 2
</code>
The reason is that in Python3, <code>bytes</code> is a type, not a function.

