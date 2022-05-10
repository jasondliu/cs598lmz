import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = b'\x00'
    m.flush()

with open('test', 'rb') as f:
    content = f.read()
    print(content)
</code>

