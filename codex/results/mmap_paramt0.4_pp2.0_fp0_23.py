import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
    m.close()
</code>
I would expect the output to be <code>b'\x02'</code>, but it is <code>b'\x01'</code>.
I'm using Python 3.5.2 on Windows 10.

