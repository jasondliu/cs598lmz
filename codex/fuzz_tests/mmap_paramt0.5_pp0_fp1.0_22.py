import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(len(m))
    print(m[0])
    m[0] = b'\x00'
    print(m[0])
    m.close()
</code>
The output is:
<code>1
49
0
</code>

