import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a), a)
</code>
The result is:
<code>0 b''
</code>
But if I remove <code>f.truncate()</code> the result is as expected:
<code>1 b'\x00'
</code>
I found out that after <code>f.truncate()</code> the length of <code>m</code> is <code>0</code> and <code>m.size()</code> is <code>1</code>.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    print(len(m), m.size())
    a = m[:]
    print(len(a), a)
</code>
This prints:
<code>0 1
0 b''
</code>
Why is this happening?


A:

When you truncate the file, the memory-mapped region is no longer valid. You need to re-map the region after trunc
