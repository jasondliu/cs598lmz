import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    print(m.read_byte())
    
    m.seek(0)
    m.write(b'0')
</code>
Python 2.7.12 and 3.5.2. Tested on Linux and Windows.

