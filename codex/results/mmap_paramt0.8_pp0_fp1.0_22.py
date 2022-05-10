import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0]
    m[0] = 0
    m[0]
</code>
This prints <code>b'\x01'</code>, <code>b'\x00'</code>, and <code>b'\x00'</code>, which is what I'd expect.

