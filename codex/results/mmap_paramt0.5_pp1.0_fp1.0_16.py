import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')

with open('test', 'r') as f:
    print(f.read())
</code>
The file <code>test</code> contains <code>\x00</code> after this.

