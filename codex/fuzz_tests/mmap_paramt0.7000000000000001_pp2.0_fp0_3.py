import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
</code>
This gives me the byte representation of 1. I'm guessing that it depends on the underlying file system. I have yet to find a file system that does not store files in byte format.

