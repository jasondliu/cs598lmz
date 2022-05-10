import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises <code>ValueError: mmap offset is greater than file size</code>.
I'm aware that this is a corner case and that I could just reopen the file, but I'm wondering why this happens.
I found that if I open the file with <code>mmap.MAP_SHARED</code> instead of <code>mmap.MAP_PRIVATE</code>, it works. But I'm not sure why.
I'm using Python 3.6.


A:

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> argument set to <code>0</code>.
<code>mmap.mmap</code> has the following signature:
<code>mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
</code>
The <code>length</code> argument is the size of the memory-mapped file.
The documentation states:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&
