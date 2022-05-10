import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code will raise <code>ValueError: mmap offset is greater than file size</code>.
But if I change the code to:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
</code>
It will work.
So why does the order matter?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The <em>length</em> argument specifies the number of bytes to map. The entire file is mapped by default.</p>
</blockquote>
So, when you create the <code>mmap</code> object, it maps the entire file.  When you truncate the file, the <code>mmap</code> object is still mapped to the entire file, even though the file is now shorter.  When you try to access the <code>mmap</code> object, it tries to access the entire file, which is now shorter than the <code>mm
