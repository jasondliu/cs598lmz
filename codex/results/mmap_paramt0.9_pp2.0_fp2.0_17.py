import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # As should change when modifing the file.
    m.write(bytes(2))
    m.flush()
    print(m.read())

with open('test', 'rb') as f:
    print(f.read())
</code>
result:
<code>b'2'
b'2'
</code>

