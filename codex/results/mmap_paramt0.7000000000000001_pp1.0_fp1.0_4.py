import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(4))
    m.seek(0)
    print(m.read())

with open('test', 'rb') as f:
    f.seek(0)
    print(f.read())

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    print(m.read())
    m.seek(0)
    m.write(bytes(4))
    m.seek(0)
    print(m.read())

with open('test', 'rb') as f:
    f.seek(0)
    print(f.read())
</code>
This code gives me the following output:
<code>b'\x04'
b'\x01'
b'\x01'
b'\x04'
b'\x04'
</code>
I don't understand why <code>m
