import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This will work, but it will not work if you use <code>f.write(bytes(1))</code> instead of the <code>m[0] = b'\x00'</code> statement.

