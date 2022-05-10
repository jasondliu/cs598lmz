import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())
    m.resize(128)
    print(m.size())
    m.close()
</code>
Output:
<code>1
128
</code>

