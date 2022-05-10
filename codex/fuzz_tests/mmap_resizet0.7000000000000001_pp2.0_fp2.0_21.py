import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I use <code>f.truncate()</code> to make file length 0, then I read the <code>mmap</code>.
I expect to get <code>[]</code>, but I get <code>[1]</code>.


A:

According to the documentation:
<blockquote>
<p>If the file is extended, the extra memory is uninitialized.</p>
</blockquote>
So it looks like it's not actually truncating it.

