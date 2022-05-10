import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 16)
    m.write(bytes(16))
    m.seek(0)
    m.write(m[::-1])
    m.flush()
    m.close()
</code>
<code>&gt;&gt;&gt; with open('test', 'rb') as f:
...     print(f.read())
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
</code>

