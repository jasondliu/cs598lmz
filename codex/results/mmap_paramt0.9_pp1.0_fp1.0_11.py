import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 10
</code>
Results in:
<code>m[0] = 10
TypeError: 'mmap.mmap' object does not support item assignment
</code>


A:

First of all, mmap is for mapping a file as memory.
Bytes(1) is a single element list that holds a byte.
When you open a file in 'WB' mode it's empty.
If you need to write a byte '1' to a file you can do:
with open('test', 'w') as f:
f.write('\x01')
or
f.write(1)

