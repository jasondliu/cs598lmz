import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 4)
    print(repr(m))
    m[0] = b'\x00'
    m.close()

with open('test', 'rb') as f:
    print(f.read())

os.remove('test')
</code>

