import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is:
<code>b'\x01'
</code>
So, the <code>mmap</code> object is not updated after <code>truncate</code>.

