import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'rb') as f:
    a = f.read()

print(a)
</code>
Output:
<code>b''
b'\x01'
</code>
So when using <code>mmap</code>, Python doesn't seem to support truncation, as the underlying <code>munmap</code> doesn't seem to support it either.

