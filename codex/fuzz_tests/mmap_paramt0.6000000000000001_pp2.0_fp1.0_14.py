import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'1'
    print(m[:])
    m.close()
</code>
Result:
<code>b'1'
</code>

