import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I thought that <code>mmap</code> should be able to read the file even if it is truncated.
Is there a way to read the file after truncating it?


A:

The documentation says:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function may need to expand the file so that it can be accessed at the specified offset. If the file cannot be expanded, <code>&lt;code&gt;mmap()&lt;/code&gt;</code> fails.</p>
</blockquote>
So, the <code>mmap</code> object is trying to expand the file to the size it was when you created the <code>mmap</code> object.
You can't read the file after truncating it, because the <code>mmap</code> object is trying to read from the original file size.

