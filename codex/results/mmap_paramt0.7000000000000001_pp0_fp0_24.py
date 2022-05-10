import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = str(2).encode('utf-8')
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>

