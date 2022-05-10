import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # &lt;-- This is the line that throws the error
</code>
I'm wondering why this happens and if there's any way to work around it. Or is there a more efficient way to truncate a file via mmap?


A:

This is the behavior of the <code>mmap</code> class, which is why it has a <code>close()</code> method.
<code>&gt;&gt;&gt; help(mmap.mmap)
...
close() -&gt; None or (when template argument is used) an integer
    Unmap the memory.
...
</code>
When you call <code>close()</code> on an <code>mmap</code> object, it is deallocated from memory. So, in your case, you need to call <code>m.close()</code> before calling <code>f.truncate()</code>.

