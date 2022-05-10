import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get a <code>mmap.error: [Errno 22] Invalid argument</code> on the last line.
I'm not sure what the problem is. I can't find any documentation on this.

