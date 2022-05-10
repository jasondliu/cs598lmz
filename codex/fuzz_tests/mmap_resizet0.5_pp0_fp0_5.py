import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m[:] = bytes(0)
    m.close()
</code>
This code works on my machine, but is it guaranteed to work on all machines?

