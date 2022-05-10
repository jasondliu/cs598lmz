import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())
</code>
Output
<code>10
</code>

