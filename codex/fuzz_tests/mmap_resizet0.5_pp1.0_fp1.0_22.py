import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me a <code>ValueError</code> on the <code>a = m[:]</code> line.
The <code>ValueError</code> is "mmap length is zero".
I don't understand why. I'm not trying to read from the file, I'm trying to read from the mmap. The mmap is not zero bytes long, it's one byte long.
I'm using Python 3.5.2 on Windows 10.

