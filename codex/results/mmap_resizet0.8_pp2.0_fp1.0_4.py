import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
Output:
<code>\x00
</code>
I am using Python 3.3.3 on Ubuntu 14.04


A:

The <code>byte</code> objects returned by <code>mmap</code> are like any other <code>bytes</code> object - they're sequences of bytes. To get the byte as an integer, you need to index into the <code>bytes</code> object:
<code>&gt;&gt;&gt; m = mmap.mmap(f.fileno(), 0)
&gt;&gt;&gt; m[:]
b'\x01'
&gt;&gt;&gt; m[:][0]
1
</code>
<code>bytes</code> objects are iterables, so the <code>m[:]</code> above is evaluated as <code>m[0:None]</code>, and returns a slice of the bytes as a new <code>bytes</code> object. Indexing that gives you an integer value back.

