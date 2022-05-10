import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints <code>b''</code> instead of <code>b'\x01'</code>.
The same thing happens if I do <code>m.seek(0)</code> before <code>a = m[:]</code>.
I'm using Python 3.6.1 on Windows 10.
Is there a way to read the bytes from the mmap object after truncating the file?

