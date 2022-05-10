import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
Here, <code>a</code> is <code>b'\x00'</code>, but I would expect it to be <code>b'\x01'</code>.
I understand that <code>mmap</code> is not a file object and does not know about the truncation, but I would expect that <code>m[:]</code> would read the contents of the file at the time of the creation of the <code>mmap</code> object.
Is this a bug, or am I missing something?

