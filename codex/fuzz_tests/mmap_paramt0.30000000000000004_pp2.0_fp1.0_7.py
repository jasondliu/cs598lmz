import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.write(bytes(2))
</code>
This code works fine on Linux, but on Windows it fails with <code>WindowsError: [Error 87] The parameter is incorrect</code>.
Is there a way to resize a memory-mapped file on Windows?


A:

According to the documentation, you need to use <code>mmap.ACCESS_WRITE</code> when opening the file:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

