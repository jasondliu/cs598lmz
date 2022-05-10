import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))

with open('test', 'rb') as f:
    print(f.read())
</code>
This prints <code>b'\x02'</code>. However, I would like to write to the file without changing the file size. I tried the following:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    m.write(bytes(2))

with open('test', 'rb') as f:
    print(f.read())
</code>
But this prints <code>b'\x01'</code>. How can I write to the file without changing the file size?

