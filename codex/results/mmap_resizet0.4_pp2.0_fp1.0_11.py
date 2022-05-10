import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I can understand that the mmap object has a reference to the file but I don't understand why it doesn't raise an exception.
I'm using Python 3.7.4 on Windows 10.

