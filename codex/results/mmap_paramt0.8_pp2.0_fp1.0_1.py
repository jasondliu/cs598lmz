import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)

with open('test', 'rb') as f:
    print len(f.read())
</code>
I get the output:
<code>1
</code>
But I'm expecting a length of 10.  Why does this happen?  Thanks in advance!


A:

<blockquote>
<p>Why does this happen?</p>
</blockquote>
I was unable to find any official documentation for the <code>mmap.resize()</code> method, but I can tell you what it does in CPython 2.7:

Truncates the mapped region to the specified size
Updates the size of the underlying file

However, the Python file object <code>f</code> is not affected by this change.  Re-opening the file will show it has the new size.
As an alternative, <code>msync()</code> can be used to flush changes to the file.  With this, the size of the file will be the new size.

