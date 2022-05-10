import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x1f\x8b\x08')
    m.seek(0)
    print(m.readline())
    print(m.readline())

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x1f\x8b\x08')
    m.seek(0)
    print(m.readline())
    print(m.readline())
</code>
Output:
<code>b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xffE\xcc\xc9\xc9W(\xcf/\xcaI\x01\x00\x94\xe5\x92\xa9\x00\x00\x00'
b'\x00'
b''
b''
</code>


A:

I think the problem is that you need to flush the buffer before you seek.
