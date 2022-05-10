import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.flush()
    m[0] = bytes(3)
    m.flush()

with open('test', 'rb') as f:
    print(f.read(1))
</code>
This outputs <code>b'\x03'</code>. I think the results are what you would expect, since <code>m.flush()</code> is required to write to the file.

