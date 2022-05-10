import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is <code>b'\x01'</code>, not <code>b'\x02'</code>.
I'm using Python 3.5.1 on Ubuntu 16.04.

