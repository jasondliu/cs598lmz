import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:]
    c = m[:]
</code>
I get a <code>ValueError: mmap offset is greater than file size</code> when I try to access <code>m</code> after I truncate the file.
I'm using Python 3.7.1 on Windows 10.
Is there a way to truncate the file and still access the memory-mapped data?

