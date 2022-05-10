import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
</code>
although in principle it should be possible to write the file <code>test</code> with <code>m.write</code> and then read the results back with <code>f.read</code>.

