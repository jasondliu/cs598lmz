import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises the exception:
<code>ValueError: mmap offset is greater than file size
</code>
I am using Python 3.8.5 on Ubuntu 20.04.

