import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I am trying to understand why the last line throws a ValueError, since I am not trying to access the file anymore.


A:

You opened the file in read-write mode, so you can do both read and write operations on the file. When you truncate the file, the mmap object becomes invalid, because the file size is changed. The mmap object is tied to the file size, so it can't be used to access the file anymore.

