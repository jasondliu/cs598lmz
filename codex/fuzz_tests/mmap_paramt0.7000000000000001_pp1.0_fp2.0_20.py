import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'a'
    print(m[0])
    m.close()
</code>
This code works with both Python 2.7 and 3.5.

