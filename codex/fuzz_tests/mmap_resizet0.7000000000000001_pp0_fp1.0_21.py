import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
The main problem is that I can't create a new <code>mmap</code> instance, because I don't know the size of the new file.
Is there a way to resize an existing <code>mmap</code> instance, or at least to obtain the size of the file it's mapped to?

