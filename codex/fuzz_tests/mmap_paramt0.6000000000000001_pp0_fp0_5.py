import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
</code>
and the <code>test</code> file is still full of <code>1</code>s.
How can I change the contents of the file without having to close it?

