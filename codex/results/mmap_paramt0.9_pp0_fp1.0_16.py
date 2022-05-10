import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m[0] = ord('a')
    m.close()

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_READ)
    print(m)
    print(m[0])
</code>
This returns
<code>&lt;mmap.mmap at 0x10a07a310&gt;
97
</code>
Please note that f.write(b'a') did not work.

