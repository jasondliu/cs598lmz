import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I think that the output should be <code>b'\x01'</code>.
Why is the output <code>b'\x00'</code>?
I'm using Python 3.6.5 on Ubuntu 18.04.


A:

The file is truncated before you read from the mmap. The mmap is not updated to reflect the truncation.

