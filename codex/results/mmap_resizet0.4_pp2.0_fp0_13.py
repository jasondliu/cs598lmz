import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints <code>b''</code> but I would expect it to print <code>b'\x00'</code>.
If I change the line <code>f.truncate()</code> to <code>f.truncate(0)</code> then it works as expected.
I've read the documentation for <code>truncate</code> and it says that the default is to truncate to the current position. So I would expect the file to be truncated to length 0 and the mmap to still be valid.
I'm using Python 3.6.1 on Windows 10.

