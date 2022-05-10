import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'\x02'
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Prints:
<code>b'\x02'
</code>

