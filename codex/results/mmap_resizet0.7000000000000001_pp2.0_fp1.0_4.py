import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
After this code the file size is 0, but the <code>a</code> is <code>b'\x00'</code>.
How is this possible?
I'm using python3.6.3, but I think the same behavior was in python3.5.

