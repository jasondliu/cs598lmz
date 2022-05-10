import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)

with open('test', 'rb') as f:
    print(f.read())
</code>
This prints:
<code>b'\x01'
b''
</code>
So, for me, the <code>mmap</code> is not valid anymore after <code>truncate</code>, and it is possible to read the data before <code>truncate</code>.

