import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws <code>ValueError: mmap offset is greater than file size</code>
How can I truncate the file and still be able to read from the mmap?


A:

You can't.  The mmap object is tied to the file descriptor, which is tied to the file.  You can't change the size of the file without invalidating the mmap.  You can, however, create a new mmap object to the new file.

