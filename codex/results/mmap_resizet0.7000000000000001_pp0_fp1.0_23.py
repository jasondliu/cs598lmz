import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # there is no data in the file
</code>
Is there a way to get data from the file when truncating it if I already have the mmap object? I could create a new mmap after truncating, but this does not seem very elegant.

