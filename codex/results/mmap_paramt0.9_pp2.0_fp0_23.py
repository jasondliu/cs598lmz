import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ | mmap.ACCESS_WRITE)
    print(m[:])
    print(m[0])
    print(m.tell())
    print(m.read(1))
    print(m.tell())
</code>
Output:
<code>b'\x01'
497
b'\x01'
1
</code>
What does <code>mmap.mmap</code> returns in Python 3?
Why does <code>read(1)</code> make <code>tell</code> return <code>1</code> instead of <code>0</code>?
If <code>tell</code> works as expected then why does <code>read(1)</code> return <code>\x01</code>?


A:

It returns a <code>memoryview</code> object:
<code>&gt;&gt;&gt; mmap.mmap(..)
&lt;memory at 0x7f6e22116f28&gt;
&gt;&gt;&gt;
