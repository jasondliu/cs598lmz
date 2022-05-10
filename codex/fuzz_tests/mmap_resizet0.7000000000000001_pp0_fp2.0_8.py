import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)  # prints b''
</code>
Prints:
<code>b''
</code>
How to make it print <code>b'\x01'</code>?

