import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The first call to <code>m[:]</code> returns the expected <code>b'\x01'</code> but the second one returns <code>b''</code>.
I have checked that if I don't call <code>truncate()</code> in the second run, I get <code>b'\x01'</code> as expected.
I also tried adding a <code>m.seek(0)</code> before the second call to <code>m[:]</code> but it doesn't change anything.
Note that I'm using Python 3.4.1 on Linux.


A:

The mmap module docs say that:
<blockquote>
<p>It is important to keep a reference to the instance of the <code>&lt;code&gt;mmap&lt;/code&gt;</
