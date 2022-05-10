import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 1
    m.close()
</code>
This works just fine. But if I do the same thing with a file that is open for writing, it fails.
<code>with open('test', 'wb') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 1
    m.close()
</code>
This throws <code>mmap.error: [Errno 22] Invalid argument</code>. I can't find anything in the documentation that says that the file needs to be opened for reading.
I'm using Python 3.5.1 on Ubuntu 16.04.


A:

You need to open the file in read/write mode.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 1
    m.close()
</code>

