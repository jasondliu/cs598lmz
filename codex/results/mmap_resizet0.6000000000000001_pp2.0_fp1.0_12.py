import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:]
    c = m[:]
    print(len(a), len(b), len(c))
</code>
Now, this program produces the output
<code>0 0 0
</code>
yet I was expecting to get
<code>1 1 1
</code>
Why is this happening?


A:

From the <code>mmap</code> docs:
<blockquote>
<p>If a file is truncated or grown while a mapping exists, the contents of the mapping are undefined, and any attempt to use the mapping may cause a segmentation fault.</p>
</blockquote>

