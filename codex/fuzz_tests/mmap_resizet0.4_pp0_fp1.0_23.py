import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
How can I truncate the file without raising an exception?


A:

You can't.
The mmap module is a wrapper around the mmap system call, which maps a file into memory.  When you truncate the file, you're removing the data that the mmap is pointing to.  The mmap object has no way of knowing that this has happened.

