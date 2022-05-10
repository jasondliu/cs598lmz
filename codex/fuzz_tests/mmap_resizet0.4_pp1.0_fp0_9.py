import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get <code>ValueError: mmap can't extend file to larger than 2GB</code>.
I know that I can use <code>mmap.ALLOCATIONGRANULARITY</code> to get the size of the memory page, but I don't know how to use it to fix my problem.

