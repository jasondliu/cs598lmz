import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'a'
    m.close()

with open('test', 'r') as f:
    print(f.read())

with open('test', 'r') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read())
    m.close()
</code>
The output:
<code>a
a
</code>

