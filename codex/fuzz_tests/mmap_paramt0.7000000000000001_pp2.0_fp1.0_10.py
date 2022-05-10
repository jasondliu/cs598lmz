import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[:] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
<code>rb</code> mode is needed and <code>m[:] =</code> should be used instead of <code>m.write</code> because <code>mmap.write</code> will write bytes after current file position, so in this case it will write bytes at the end of file.

