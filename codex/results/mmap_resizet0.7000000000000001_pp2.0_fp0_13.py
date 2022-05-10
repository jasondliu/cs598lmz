import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I am wondering why the last line raises <code>ValueError: mmap offset is greater than file size</code>?


A:

This is because a <code>mmap</code> object is not a simple wrapper around the file. The <code>mmap</code> object is a wrapper around kernel memory where the file is mapped and is associated with file descriptors, which are used for I/O operations.
When you truncate the file, the kernel is no longer able to locate the file descriptor which was used to create the <code>mmap</code> object.

