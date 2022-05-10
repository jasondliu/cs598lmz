import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
    print(m.read(1))
    m.close()
</code>
The output is <code>b'\x02'</code> and <code>b'\x00'</code>. But I expected <code>b'\x01'</code> and <code>b'\x02'</code>.
Why is the first byte overwritten?

