import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get a <code>ValueError</code>:
<blockquote>
<p>ValueError: mmap offset is greater than file size</p>
</blockquote>
I suspect this is because the file is now empty (I don't know if mmap is actually checking the file size or not). The documentation states that <code>mmap</code> will raise an exception when the file size is smaller than the offset, but I don't see that happening.
If I change the code to:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate(0)
    a = m[:]
    m.close()
</code>
the code runs without error.
Is it safe to assume that <code>mmap</code> is taking the file size into account when determining whether the offset is valid?


A:

The documentation is wrong
