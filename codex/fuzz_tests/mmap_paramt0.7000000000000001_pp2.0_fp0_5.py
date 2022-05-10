import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.write(b'\x00\x00')

with open('test', 'rb') as f:
    print(f.read().decode(), end='')
</code>

