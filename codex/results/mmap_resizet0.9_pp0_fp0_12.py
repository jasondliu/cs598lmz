import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It worked:
<code>&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
...     a = m[:]
...
&gt;&gt;&gt; a
b'\x00'
</code>
As many bytes as there are in truncated file are read from mmap.

