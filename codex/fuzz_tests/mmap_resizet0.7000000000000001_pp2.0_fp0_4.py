import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
This is the output:
<code>b'\x01'
</code>
As you can see, there's a byte <code>b'\x01'</code> in the <code>m</code>.

