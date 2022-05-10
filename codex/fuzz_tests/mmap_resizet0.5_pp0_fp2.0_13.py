import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This will print <code>b'\x00'</code> instead of <code>b'\x01'</code>. Is there any way to get the original contents of the file before truncating?
I am using Python 3.6.3 on Windows 10.

