import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.close()
</code>
The problem is that <code>m.read(1)</code> returns <code>b'\x01'</code> instead of <code>b'\x00'</code>.
What am I doing wrong?


A:

<code>bytes</code> will create a sequence of bytes with a length of 1 and a value of 1, which is <code>\x01</code>
<code>&gt;&gt;&gt; bytes(1)
b'\x01'
</code>
You want to use <code>bytes(1)</code> to create a sequence of bytes with a length of 1 and a value of 0, which is <code>\x00</code>
<code>&gt;&gt;&gt; bytes(1)
b'\x00'
</code>

