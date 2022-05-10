import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I can't understand why this happens.
I know that <code>m[:]</code> returns a copy of the memory map, and <code>m[:]</code> is not affected by <code>f.truncate()</code> if it is called after <code>m[:]</code>.
But I can't understand why <code>m[:]</code> returns <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I expected that <code>m[:]</code> returns <code>b'\x01'</code> because <code>m[:]</code> returns a copy of the memory map.
I expected that <code>m[:]</code> returns <code>b'\x01'</code> because <code>m[:]</code> is not affected by <code>f.truncate()</code> if it is called after <code
