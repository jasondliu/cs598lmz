import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m[0] = b'\x01'
    m[0] = b'\x02'
    m[0] = b'\x03'
    m[0] = b'\x04'

with open('test', 'r+b') as f:
    print(f.read())
</code>
The output is:
<code>\x04
</code>

