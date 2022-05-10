import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
    m.close()
</code>
It prints <code>b'\x02'</code> and the file <code>test</code> contains <code>\x02</code>.

