import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
</code>
<blockquote>
<p>b'\x01'</p>
</blockquote>

