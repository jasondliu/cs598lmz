import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I would expect this to print <code>b'2'</code>, but it prints <code>b'1'</code>.
I'm using Python 3.8.1 on Windows 10.

