import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.flush()

with open('test', 'rb') as f:
    f.read()
</code>
You can also try <code>m.close()</code> after the flush.

