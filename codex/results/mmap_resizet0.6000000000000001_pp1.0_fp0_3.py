import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I'm using Python 3.7.3.
I assumed that <code>f.truncate()</code> should not do anything as the file is already empty.
I'm trying to understand the behavior of the code above.


A:

From the documentation:
<blockquote>
<p>The <code>&lt;code&gt;truncate()&lt;/code&gt;</code> method truncates the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed.</p>
</blockquote>
So it seems that truncating to 0 is the default.

