import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<code>b'\x01'
</code>
Note that I'm using <code>r+b</code> instead of <code>rb</code> to be able to change the file length.

