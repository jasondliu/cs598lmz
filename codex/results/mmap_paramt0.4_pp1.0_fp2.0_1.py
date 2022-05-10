import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x02'
    m.close()
</code>
The file 'test' will contain the byte <code>2</code> instead of the byte <code>1</code>.

