import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:]
    print(a, b)  # works
</code>
Bonus:
<code>&gt;&gt;&gt; print(a, b)
b'\x01' b'\x01'
</code>

