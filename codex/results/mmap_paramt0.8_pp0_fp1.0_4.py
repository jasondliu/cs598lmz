import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.move(1, 0, 1)
    m.move(0, 1, 1)

with open('test', 'rb') as f:
    print f.read()
</code>
prints <code>\x01</code> instead of <code>\x00</code>.


A:

Your file contains <code>\x00</code>, not <code>\x01</code>. If you want to write <code>\x01</code> to the file, use
<code>f.write(b'\x01')
</code>

