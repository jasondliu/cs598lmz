import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>

<code>&gt;&gt;&gt; a
b'\x00'
</code>

<code>&gt;&gt;&gt; m[:]
b'\x01'
</code>

<code>&gt;&gt;&gt; m.seek(0)
0
&gt;&gt;&gt; m.read()
b'\x01'
</code>

<code>&gt;&gt;&gt; m.tell()
0
&gt;&gt;&gt; m.seek(0, 2)
1
&gt;&gt;&gt; m.tell()
1
&gt;&gt;&gt; m.seek(0)
0
&gt;&gt;&gt; m.read()
b'\x01'
</code>

<code>&gt;&gt;&gt; bytes(m.read())
b'\x01'
</code>

