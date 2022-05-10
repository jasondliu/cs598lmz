import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    print(m)
    print(m[0])

    m[0] = bytes(2)

    print(m[0])

    m.close()

with open('test', 'rb') as f:
    data = f.read()
    print(data)
</code>
Giving the output:
<code>&lt;mmap.mmap object at 0x7fa5b5e53f70&gt;
1
2
b'\x02'
</code>

