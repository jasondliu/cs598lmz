import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
raises:
<code>mmap.error: [Errno 22] Invalid argument
</code>
How can I truncate the file without getting the <code>mmap.error</code>?


A:

The error you're seeing is because the <code>mmap</code> object is trying to access memory on the old file after it was truncated.  The mmap object is also a file-like object, so you can just truncate the mmap instead:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.truncate()
    a = m[:]
</code>
Note, however, that this may not do what you expect if you're trying to clear the file, since it will only clear the mapped part of the file:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0
