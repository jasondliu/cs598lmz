import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 5
    m.flush()
</code>
Is there an intention reason it's not possible to directly write the number into the mmap object?
Update
Looking at creating an in-memory mmap, it seems it's not possible to assign a single byte.
<code>&gt;&gt;&gt; m = mmap.mmap(-1, 2)
&gt;&gt;&gt; m[0] = 10
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: an integer is required
</code>


A:

In Python 2, <code>ord</code> returns no meaningful information:
<code>&gt;&gt;&gt; ord('5')
53
</code>
More specifically, no value can be converted to a single <code>bytes</code> object.  Mapping a write operation to an integer is therefore pointless and not provided.
In Python 3 on the other hand, strings are <code>bytes</code> objects and you
