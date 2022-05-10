import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
Outputs:
<code>b'\x00'
</code>
Expected:
<code>b'\x01'
</code>
This is true even if you add:
<code>m.flush()
f.flush()
</code>

