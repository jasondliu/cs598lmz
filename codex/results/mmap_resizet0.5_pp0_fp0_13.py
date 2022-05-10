import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the last line to raise <code>ValueError: mmap offset is greater than file size</code> because <code>f.truncate()</code> truncates the file to 0 bytes. But it doesn't. What am I missing?

