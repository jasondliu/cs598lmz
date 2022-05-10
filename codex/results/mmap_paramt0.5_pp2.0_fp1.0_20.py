import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    print(m[0])
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>1
b'\x02'
</code>

