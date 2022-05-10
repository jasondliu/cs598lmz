import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read()) # 1
    m.seek(0)
    m.write(bytes(2))
    m.close()

with open('test', 'rb') as f:
    print(f.read()) # 2
</code>

