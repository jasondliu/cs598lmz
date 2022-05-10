import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

assert a == bytes(1)
</code>
The file should remain open until we <code>close()</code> it or the object is garbage collected. 

