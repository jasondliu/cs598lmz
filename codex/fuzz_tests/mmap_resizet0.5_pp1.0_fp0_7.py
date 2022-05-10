import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting <code>ValueError: mmap closed or invalid</code> on the last line. What's the problem?
I'm using Python 3.6.3 on Windows 10.

