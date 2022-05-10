import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m[0] = 2
    
with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'\x01'
b'\x02'
</code>

