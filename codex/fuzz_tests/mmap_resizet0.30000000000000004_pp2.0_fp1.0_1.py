import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b''</code>.
I expected <code>b'\x00'</code>.
Why is the output <code>b''</code>?
How can I get <code>b'\x00'</code>?

