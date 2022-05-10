import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>


A:

The problem is that <code>m[0] = bytes(2)</code> does an implicit <code>int(2)</code> and <code>int(bytes(2))</code> is <code>0</code>, so you are still writing a single <code>\x00</code> byte.
As stated in the documentation, you can use the <code>memoryview</code> to avoid this:
<blockquote>
<p>A memoryview is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to share memory between data-structures (things like PIL images, SQLlite databases, NumPy arrays, etc.) without first copying. This is very important for large data sets.</p>
</blockquote>
So you can use:
<code>m[0] = memoryview(bytes(2))
</code>
(or better <code>m[0:2] = memoryview(b'\x01\x02')</code>)

