import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # ValueError: Cannot read from closed file
</code>
I'm trying to truncate a file while mmap object is open. But it fails with 'Cannot read from closed file'. Is there way to truncate file with mmap object?

