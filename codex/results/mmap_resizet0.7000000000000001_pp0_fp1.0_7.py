import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Is it possible to prevent this without having to create a copy of the file?


A:

No, it is not possible.
What you are asking for is impossible because of the way the operating system is designed. POSIX guarantees that mmap'd data is consistent with the actual file, but says nothing about the state of the file descriptor.
In other words, you are guaranteed that if you open a file, mmap it, and then mmap the same file again, then you have two mmap'd regions that are consistent with each other. However, there is no guarantee that two different file descriptors for the same file are consistent with each other.
Therefore, the behavior you are seeing (the file descriptor pointing to the end of the file) is the correct behavior according to the POSIX standard.
If you want to continue using mmap and truncate, you will have to mmap the file twice: once for reading and once for writing.

