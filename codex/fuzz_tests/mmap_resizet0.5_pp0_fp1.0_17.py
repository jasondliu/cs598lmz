import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get a <code>ValueError</code> on the <code>m[:]</code> line.
<code>ValueError: mmap length is zero
</code>
What am I doing wrong?

