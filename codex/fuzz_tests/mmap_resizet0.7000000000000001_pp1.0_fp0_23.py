import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
So is the <code>mmap</code> allowed to not have any bytes to map in this case?


A:

A mmap can't have no bytes. It must have at least one.
You can't mmap an empty file, because the address space would have no bytes mapped to it.

