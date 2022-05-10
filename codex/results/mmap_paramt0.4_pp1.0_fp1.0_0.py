import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'\xff')
    print(m.read_byte())
    m.seek(0)
    print(m.read_byte())
</code>
This prints <code>-1</code> and <code>-1</code> (which is the same as <code>255</code>).

