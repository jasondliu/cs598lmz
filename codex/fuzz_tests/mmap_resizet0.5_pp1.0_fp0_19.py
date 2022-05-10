import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This gives me a <code>ValueError</code>:
<code>ValueError: mmap can't extend file to larger than 2GB on 32-bit system
</code>
I have no idea where this <code>2GB</code> limit comes from.
I'm running Python 3.5.2 on a 64-bit Windows 7 system.

