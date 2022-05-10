import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = 2
    print(m[0])
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
If you run this code, you will see that the file contains the byte <code>b'\x02'</code> at the end.

