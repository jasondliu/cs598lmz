import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = bytes(2)

with open('test', 'rb') as f:
    print(f.read())
</code>
This is what I get:
<code>b'\x02'
</code>

