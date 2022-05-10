import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m.write(bytes(2))
    print(m[:])
    m.seek(0)
    print(m[:])
    m.close()
</code>
Output:
<code>&lt;mmap.mmap object at 0x7f1b6d1c6d80&gt;
b'\x02'
b'\x02'
</code>

