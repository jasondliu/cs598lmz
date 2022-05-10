import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
I expected that <code>a</code> would be <code>b'\x01'</code>, but it is <code>b''</code>.
What is a correct way to get the contents of a file after truncation?

