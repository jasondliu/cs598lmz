import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 4)
    m.resize(4)

with open('test', 'rb') as f:
    print(f.read())
</code>
this prints 
<blockquote>
<p>b'\x01\x00\x00\x00'</p>
</blockquote>

