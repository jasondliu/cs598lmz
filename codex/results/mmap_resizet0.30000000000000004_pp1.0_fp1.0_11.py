import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize</code> to fix this. But I think it is not a good idea to use <code>mmap.resize</code> in this case.
So, I have two questions:

Why does <code>mmap</code> raise <code>ValueError</code>?
How can I fix this?



A:

<blockquote>
<p>Why does mmap raise ValueError?</p>
</blockquote>
Because the file is truncated, and the <code>mmap</code> object is still pointing at the old file.
<blockquote>
<p>How can I fix this?</p>
</blockquote>
You can't. You need to close the <code>mmap</code> object before truncating the file.

