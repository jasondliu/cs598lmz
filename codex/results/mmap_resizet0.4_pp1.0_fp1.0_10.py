import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises an error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
How can I truncate a file while keeping the mmap valid?

