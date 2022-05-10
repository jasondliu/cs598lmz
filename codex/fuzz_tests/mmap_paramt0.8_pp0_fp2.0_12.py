import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m[1] = b'\x02'
    m[2] = b'\x03'
    m[3] = b'\x04'
    m[4] = b'\x05'
    m[5] = b'\x06'
    m[6] = b'\x07'
</code>
I end up with a 7 byte file, the first byte being 0, the next 6 being 2-7.

