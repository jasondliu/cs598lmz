import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # This raises an exception.
</code>
The reason is that the <code>mmap</code> object is then referring to a memory map of length 0, which is illegal.
You can simply avoid this by closing the <code>mmap</code> object before truncating the file:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
</code>

