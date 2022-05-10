import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
On line 11, I get the error <code>mmap.error: [Errno 22] Invalid argument</code>. If I comment out line 10, everything works fine.
I know that I could use <code>m.resize()</code> instead of <code>truncate()</code>, but I am using this as a simplified example of a more complex problem.
Why does the <code>truncate()</code> call fail, and is there any way to get around it?


A:

The problem is that <code>truncate()</code> causes the file to be resized, which means that the mmap object is no longer valid.  This is explained in the documentation for <code>mmap</code>:
<blockquote>
<p>mmap.mmap(...)</p>
<p>...</p>
<p>Note that modifying the mmap’ed data stores it back to the file. However, modifications are not seen by other programs that have the file open until the modifications are flushed or the file is closed. To force a flush, call the flush() method or use
