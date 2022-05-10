import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(5))
    print("fileno: " + str(m.fileno()))
</code>
With the above example, the byte count of <code>test</code> remains at 1. If I set <code>m = mmap.mmap(f.fileno(), 5)</code> the byte count goes up to 6, but the string isn't actually set. Using <code>m[:]</code> I can see the contents of what it should be and the length of <code>m</code> changes, but nothing seems to get stuck in the file.


A:

When I edit your example, the code is working for me:
<code>import mmap

#create test.bin with 1 byte
with open('test.bin', 'wb') as f:
    f.write(bytes(1))

#map file test.bin in read/write mode
with open('test.bin', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(5))
    print("
