import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises a <code>ValueError</code>:
<code>ValueError: mmap can't extend file to length 0
</code>
I understand why this happens, but I'm wondering if there is a way to avoid it. I'm using Python 3.6.

