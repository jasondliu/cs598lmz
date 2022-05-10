import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
</code>
the file size doesn't change.
<code>$ ls -l test
-rw-r--r--  1 user  staff  1 Apr 20 16:57 test
</code>
However, I can see the new size if I open the file again:
<code>with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.size())
</code>
<blockquote>
<p>2</p>
</blockquote>
What's going on here?
I am using Python 3.6.3 and macOS 10.12.6.


A:

You need to call <code>flush()</code> on the <code>mmap</code> instance after the <code>resize()</code> call:
<code>m.resize(2)
m.flush()
</code>
From the docs:
<blockquote>
<p><code>&lt;code&gt;flush()&lt;/code&gt;</
