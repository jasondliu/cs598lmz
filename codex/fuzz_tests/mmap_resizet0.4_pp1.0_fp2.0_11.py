import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect that <code>a</code> would be an empty <code>bytes</code> object, but instead it is a <code>bytes</code> object with a single <code>0</code> in it.
The documentation for <code>mmap.mmap</code> says that:
<blockquote>
<p>The file’s size cannot be changed while mmap() is in use.</p>
</blockquote>
But it doesn't say what happens if you try to do so.
The documentation for <code>mmap.mmap.resize</code> says:
<blockquote>
<p>This method is only supported on Windows. On Unix, it raises <code>&lt;code&gt;ValueError&lt;/code&gt;</code>.</p>
</blockquote>
But it doesn't say what happens if you try to change the size of the file in some other way.
I'm using Python 3.6 on Linux.

