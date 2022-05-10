import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    print(m[:])
</code>
This gives output:
<code>b'\x01'
b''
</code>
The first <code>print</code> is what I expect, the file is deleted but the <code>mmap</code> object still has the same data.
The second <code>print</code> is what I expect, the file is deleted and the memory mapped data is also deleted.
The third <code>print</code> is what I expect, the file is deleted and the memory mapped data is also deleted.
The problem is that the second and third <code>print</code> give the same output.
How do I get the second <code>print</code> to give different output from the third <code>print</code>?


A:

This is a bug in the standard library, which is fixed in Python 3
