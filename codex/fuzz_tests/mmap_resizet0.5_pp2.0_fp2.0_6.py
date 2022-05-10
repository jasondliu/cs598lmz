import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives me an <code>mmap.error: [Errno 9] Bad file descriptor</code>.
How can I get the bytes from the <code>mmap</code> object after I truncate the file?


A:

You can't.  Once you truncate the file, the memory map is invalidated.

