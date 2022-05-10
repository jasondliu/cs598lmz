import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.close()
</code>
Is there any way to do this without having to close the mmap and reopen it?

