import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect the last line to throw an exception because the <code>mmap</code> object is no longer valid. However, the program just exits normally.
Is this expected behavior? Is there a way to get a <code>mmap</code> object to throw an exception when the underlying file is truncated?


A:

This is documented behavior:
<blockquote>
<p>If the file is resized, either by another process or by using <code>&lt;code&gt;mmap.resize()&lt;/code&gt;</code>, any references to the memory beyond the new size will return undefined data, and the next access beyond the new size will raise a <code>&lt;code&gt;SIGBUS&lt;/code&gt;</code> signal on Unix systems.</p>
</blockquote>
So, if you want to check if the file has been resized, you can use <code>mmap.resize()</code> with a size that is smaller than the current size of the file.

