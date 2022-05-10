import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print('a', a)
    m.close()
</code>
The output is <code>a b''</code>.
I was expecting <code>a b'\x01'</code>.

