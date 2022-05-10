import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'r') as f:
    print(f.read())
</code>
which outputs
<code>
</code>
The file is truncated, but the mmap instance still refers to the original file size. The docs state that:
<blockquote>
<p>It is safe to resize the file while it is mapped, and the mappings will be updated accordingly.</p>
</blockquote>
But this is not happening.


A:

The documentation of <code>mmap.mmap</code> states:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is omitted, the current length of the file is used.</p>
</blockquote>
…which is what you're doing.
If you want to map the whole file, use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)</code> instead.

