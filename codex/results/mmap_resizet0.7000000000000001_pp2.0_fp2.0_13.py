import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
This will <code>mmap</code> the file and then truncate it. I would expect this to fail (or at least it should not be possible to read from the <code>mmap</code>ed region), since the file is now truncated. But instead this prints <code>b'\x01'</code>. Why does this work? How does <code>mmap</code> still know where the data is if the file is truncated?

