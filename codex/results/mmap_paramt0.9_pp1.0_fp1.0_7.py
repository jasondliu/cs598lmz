import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'0'[0]
</code>
Is <code>mmap.mmap.write</code> necessary? It's unclear if you require <code>bytes</code> or <code>bytearray</code> here:

<code>bytes</code> are immutable
<code>bytearray</code> are mutable

If the file is memory-mapped, then, the code above should not fail without <code>write</code>, right?

