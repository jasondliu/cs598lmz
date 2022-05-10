import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'9'
</code>
It seems to (successfully) replace the byte, but when I open the file in a hex editor, I see the original value. How can I replace bytes in a file?


A:

When using <code>mmap</code>, you need to <code>flush</code> the memory mapped object after you are done with it.
<blockquote>
<p>Note that changes to the mapped value will not be reflected in the file. If you want to flush changes to disk, use the flush() method.</p>
</blockquote>
<code>&gt;&gt;&gt; m = mmap.mmap(f.fileno(), 0)
&gt;&gt;&gt; m[0] = b'9'
&gt;&gt;&gt; m.flush()
&gt;&gt;&gt; m.close()
</code>

