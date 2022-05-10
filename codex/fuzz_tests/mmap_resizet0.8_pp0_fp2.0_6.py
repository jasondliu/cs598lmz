import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

with open('test2', 'wb') as g:
    g.write(a)
</code>
This small program takes a file and writes one byte, then maps the file, truncates it and writes the mapped byte to another file.
From the docs I don't see any reason why the mapped byte should not be preserved, but the output file is instead empty.
What am I doing wrong?


A:

First, you need to <code>close()</code> the <code>mmap</code> instance before calling <code>truncate()</code> or actually writing to the file.  Second, even if you do this, you will not be able to <code>truncate()</code> the file to a length of zero.  The docs are explicit about this:
<blockquote>
<p>A <code>&lt;code&gt;ValueError&lt;/code&gt;</code> is raised if the new length would be larger than the file’s current size.</p>
</blockquote>
Perhaps you could use <code>m.tell()</code
