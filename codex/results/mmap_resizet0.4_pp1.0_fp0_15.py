import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
The documentation says:
<blockquote>
<p>If the file is resized by another program or by a call to os.truncate() in the same process in which mmap() was called, the contents of the memory map as well as the values returned by size() and tell() may be incorrect. To rectify this, you can re-initialize the memory map using m.seek(0, 0) and m.resize().</p>
</blockquote>
So I tried <code>m.seek(0, 0)</code> and <code>m.resize()</code> but got <code>OSError: [Errno 22] Invalid argument</code>.
How do I fix the memory map after truncating the file?


A:

<code>m.resize()</code> is not a method of the <code>mmap</code> class. It is a method of the <code>mmap.mmap</code> class.
<code>with open('test', 'r
