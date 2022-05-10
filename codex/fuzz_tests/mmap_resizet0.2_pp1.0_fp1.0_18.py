import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The result is <code>b'\x00'</code> instead of <code>b'\x01'</code>.
Is there a way to get the correct result?


A:

The problem is that the file is truncated before the <code>mmap</code> object is created.
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
</code>

