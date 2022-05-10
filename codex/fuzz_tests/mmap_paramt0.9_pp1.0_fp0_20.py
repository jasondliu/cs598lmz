import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
</code>
On python 2.7 I get a TypeError: an integer is expected, got str.
According to the documentation http://docs.python.org/library/mmap.html#mmap.mmap I should be able to write a "bytearray" to the file.
What is wrong?


A:

The argument to <code>mmap.write</code> is expected to be a string.
In Python 2, <code>bytes</code> was a string type.  In Python 3, <code>bytes</code> is a distinct type, designed for handling binary data.
In Python 3, to create a byte string (for writing to a <code>mmap</code>), use:
<code>bytes([1])
</code>

