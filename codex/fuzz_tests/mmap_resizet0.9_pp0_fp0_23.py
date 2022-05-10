import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
All the operations I try result in the mmap object having an empty string.
Note: In reality, I do not have an initial byte, but I was able to reproduce this behavior with a byte.

