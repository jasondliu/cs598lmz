import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(ord(m[0])+1)

with open('test', 'r+b') as f:
    print(f.read())
</code>
output:
<code>b'\x02'
</code>

