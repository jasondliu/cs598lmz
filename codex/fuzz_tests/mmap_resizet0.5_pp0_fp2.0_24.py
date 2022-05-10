import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This prints <code>b'\x00'</code> instead of <code>b'\x01'</code>
Note that if I use <code>mmap.mmap(f.fileno(), 1)</code> instead, it prints <code>b'\x01'</code>.
Is this a bug or expected behavior?

