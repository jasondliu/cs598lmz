import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x01'
    m.flush()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x01'
    m.flush()
</code>
This fails on the second <code>mmap</code> call with:
<code>ValueError: mmap can't extend file to length 0x1: Invalid argument
</code>
Any idea why?

