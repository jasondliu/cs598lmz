import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Will result in an <code>ValueError: mmap closed or invalid</code> exception.
I think the file object is not invalidated when the file was truncated (at least for the file descriptor) - is there a way to get the remaining data from the mmap?

