import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = '0'
    m.seek(0)
    print m.read(1)
</code>
When running, it prints:
<code>1
</code>
Where do I lose one byte?

