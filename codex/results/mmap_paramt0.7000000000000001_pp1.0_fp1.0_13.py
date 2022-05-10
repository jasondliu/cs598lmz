import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'0'
    print(m[0])
    m.close()
</code>


A:

You can use <code>mmap.ACCESS_READ</code> with <code>mmap.PROT_WRITE</code> to get the desired behavior.
This code sample works for me:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ, prot=mmap.PROT_WRITE)
    m[0] = b'0'
    print(m[0])
    m.close()
</code>

