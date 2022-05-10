import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is <code>b''</code>, but I want it to be <code>b'\x01'</code>.
How can I make the mmap object "see" the truncated file?

