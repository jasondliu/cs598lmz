import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    print(m[0])
    print(m[0:])
    print(m[1:])
    print(m[:])

    m.write(b'2')
    print('wrote 2')
    print(m[0])

    m.seek(0)
    print('seek 0')
    print(m[0])
</code>
Output:
<code>&lt;mmap.mmap object at 0x10eba1f90&gt;
49
b'1'
b''
b'1'
wrote 2
50
seek 0
50
</code>
Docs: https://docs.python.org/3.6/library/mmap.html

