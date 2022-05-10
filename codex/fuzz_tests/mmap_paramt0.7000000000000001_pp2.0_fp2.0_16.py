import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m[:] = bytes(2)
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
This prints
<code>b'\x01'
b'\x02'
</code>
Which is what I expected. I don't know what you were doing, but the code you posted should work.

