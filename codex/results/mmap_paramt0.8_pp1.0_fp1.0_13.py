import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    if m.read(1) == b'0':
        m.seek(0)
        m.write(b'\xff')
    m.flush()
</code>
The assertion gets violated on the <code>m.read(1)</code> line, which is probably the "natural" way to interact with the file. Is there a way to do this with a memory map, that doesn't involve <code>os.read</code> or <code>os.write</code>?


A:

Fixing the issue with the example, you need to write <code>bytes(1)</code> (that is, create a single-byte bytes object with the value of 0) instead of just the number 1, which is an int, not a bytes object.
But that's not really the issue here. The <code>write()</code> function only replaces the bytes currently present in the file with your replacement bytes, not the bytes currently in the mmap. That means that the <code>\x00</code> byte is still in the mmap and so <code>read()</code> returns <code>b'\
