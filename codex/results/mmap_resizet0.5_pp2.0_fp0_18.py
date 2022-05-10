import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.seek(0)
    m.write(bytes(1))
    m.close()
</code>
Here, the <code>m[:]</code> accesses the memory-mapped data, which still exists despite the underlying file being truncated.
I'd like to know if there is a way to detect that this has happened.  I know I can check the file size, but I'm wondering if there is a way to detect that the file has been truncated while the memory-mapped file object is still open.


A:

No, you can't detect that the underlying file has been truncated. The only thing you can do is to try to access the memory-mapped data and handle the exception.

