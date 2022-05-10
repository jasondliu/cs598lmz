import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It seems that <code>mmap</code> uses a pointer to the file. When I truncate the file, the pointer is still pointing to the old file, but the file is empty.
How can I truncate the file with <code>mmap</code>?


A:

In Python, <code>mmap.mmap()</code> has a <code>length</code> argument, which is the size of the mapping.  When you do <code>m = mmap.mmap(f.fileno(), 0)</code>, you are creating a mapping of size 0, which means there is no mapping.  So <code>m[:]</code> will always return an empty string.  If you instead do <code>m = mmap.mmap(f.fileno(), 1)</code>, then <code>m[:]</code> will return the first byte of the file.  If you do <code>m[:] = b'\x00'</code> then you are writing 0 to the first byte of the file.  If you then do <code>f.tr
