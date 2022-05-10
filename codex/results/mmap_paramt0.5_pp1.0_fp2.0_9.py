import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>
This code prints <code>b'\x01'</code> on Python 2.7.6 and <code>b'\x02'</code> on Python 3.4.3.

