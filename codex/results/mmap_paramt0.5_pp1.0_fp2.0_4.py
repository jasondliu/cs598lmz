import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is <code>b'\x01\x01'</code> as expected.

