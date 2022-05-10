import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
but the <code>a</code> variable is empty.
I want to implement the same behavior as when I do <code>open('test', 'r+b').read()</code>.

