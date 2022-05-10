import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
If someone knows how to do this in Windows (both Posix and Windows code is acceptable), please help.


A:

I believe the Windows flavor of <code>mmap.mmap</code> doesn't allow writing to a file, only reading.  So you can't use <code>mmap</code> to change the value of the existing file.
You may be able to accomplish what you want by making the file temporarily read-only, then doing your <code>mmap</code> read, and then making the file writable again.

