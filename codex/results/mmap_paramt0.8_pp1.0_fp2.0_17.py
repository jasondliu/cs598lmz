import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
The file's first byte is changed from 1 to 2.

