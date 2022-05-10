import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It raises <code>ValueError: memory mapping closed or invalid</code>. Why?


A:

When you call <code>f.truncate()</code>, the file size is reduced to zero, invalidating the mmap.
AFAIK, the only way to truncate a file while keeping the mmap valid is to use an OS-specific API.

