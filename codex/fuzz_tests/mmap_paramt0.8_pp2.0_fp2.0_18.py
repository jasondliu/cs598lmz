import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'a'
    m.close()
</code>

<code>with open('test', 'r+b') as f:
    print(f.read(1), f.tell())
    f.seek(0)
    print(f.read(1), f.tell())
</code>
Prints:
<code>b'a' 1
b'a' 1
</code>

