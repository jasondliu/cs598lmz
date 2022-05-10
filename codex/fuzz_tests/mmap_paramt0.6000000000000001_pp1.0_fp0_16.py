import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    # 0 = read only
    # 1 = read/write
    # 2 = copy on write
    # 3 = private (copy on write)
    # 4 = private (copy on write, remove on unmap)
    m.access = 2

    # m[0] = b'\x00'
    # m[0] = b'\x00'
    m[0] = b'\x00'
    print(m)
    m.flush()
    m.close()
</code>
The output is:
<code>mmap(0, 1, access=2, offset=0)
</code>
This is different than the default value of <code>access=3</code> which is documented in the official Python docs.

