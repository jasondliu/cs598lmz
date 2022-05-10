import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2) # this will fail under python 2.x;
    #2 bytes expected, 1 byte at position 0 but only 1 bytes read
</code>

