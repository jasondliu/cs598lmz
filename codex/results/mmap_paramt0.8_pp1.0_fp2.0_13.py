import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0x40b0
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Result:
<blockquote>
<p>b'\x40\xb0'</p>
</blockquote>

