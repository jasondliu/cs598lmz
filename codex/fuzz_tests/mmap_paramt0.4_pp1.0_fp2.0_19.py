import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'\x00'
</code>

I'm using Python 3.7.3 on Windows 10.

