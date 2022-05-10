import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get <code>b'\x01'</code> as output.
I was expecting <code>b''</code> as output because I truncated the file after creating the mmap.
Why is the mmap not updated when the file is truncated?

