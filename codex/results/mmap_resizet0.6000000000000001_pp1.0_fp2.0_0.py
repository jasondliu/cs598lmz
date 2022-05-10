import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This program always prints <code>b''</code>
But if I change the line <code>m = mmap.mmap(f.fileno(), 0)</code> to <code>m = mmap.mmap(f.fileno(), 1)</code> then the program prints <code>b'\x01'</code> as expected.
Why does the first version not work?
Python 2.7.12, Windows 7 x64

