import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # Truncated file
</code>
I think it's an error in MMAP because if you don't try to read from the memory map, then it works fine.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate() # No error
</code>
I'm using Python 3.7.1 on Ubuntu 18.04.
Is this a problem with my code, or with <code>mmap</code>?


A:

Using <code>0</code> as the <code>size</code> argument of <code>mmap.mmap</code> doesn't work as you expect. According to the documentation, it says:
<blockquote>
<p><code>&lt;code&gt;size&lt;/code&gt;</code> is the number of bytes to map. The default value is the current size of the file.</p>
</blockquote
