import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Windows and Mac but throws an error on Linux.
<code>mmap.error: [Errno 22] Invalid argument
</code>
Is it expected behaviour?

