import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This produces the error <code>TypeError: 'str' does not support the buffer interface</code>
I have tried to use <code>m[0] = bytes(2)</code> as well as <code>m[0] = 2</code> and <code>m[0] = 2.to_bytes(1, 'big')</code> but they all give the same error.
How can I write a single byte to a memory-mapped file?


A:

As far as I can tell, the problem is that <code>bytes()</code> is not a type that is supported by <code>mmap</code>.
<code>&gt;&gt;&gt; m[0] = 2
&gt;&gt;&gt; m[0]
2
&gt;&gt;&gt; m[0] = 2.to_bytes(1, 'big')
&gt;&gt;&gt; m[0]
2
</code>
It doesn't matter if it's a byte or a
