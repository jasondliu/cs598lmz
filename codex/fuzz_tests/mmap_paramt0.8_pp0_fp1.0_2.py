import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'B'
</code>
Output:
<code>&gt;&gt;&gt; with open('test') as f:
...     print(f.read())
...
B
&gt;&gt;&gt;
</code>

