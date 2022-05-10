import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<code>b''
</code>
I would expect the output to be <code>b'\x01'</code>.
I am using Python 3.7.3 on Ubuntu 18.04.


A:

The mmap object is a view of the file. Truncating the file removes the data that the mmap object is viewing.

