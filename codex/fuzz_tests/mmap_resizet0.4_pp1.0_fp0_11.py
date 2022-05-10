import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code works, but I don't understand why.
I expected that <code>m[:]</code> will raise an exception, because the file was truncated. But it doesn't.
I'm using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> object is a view of the file's contents at a particular point in time. It doesn't change if you change the file's contents.

