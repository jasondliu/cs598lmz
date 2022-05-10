import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    a = m.readline()
m.close()
</code>
I receive Exception when execute m.seek(0) with:
<code>ValueError: mmap offset is greater than file size
</code>
When my file is empty. How to solve it?


A:

<blockquote>
<pre><code>&lt;code&gt;mmap offset is greater than file size
&lt;/code&gt;</code></pre>
</blockquote>
<code>seek(0)</code> means go to <code>0</code> bytes from the beginning of the file.
That's the problem, you tried to go to a positition during <code>m.seek(0)</code> which is bigger than the length of the file.

