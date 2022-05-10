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
<p>If the file is resized by another program or by a function like <code>&lt;code&gt;os.truncate()&lt;/code&gt;</code>, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object can be resized as well, using the <code>&lt;code&gt;resize()&lt;/code&gt;</code> method.</p>
</blockquote>
But I can't find any <code>resize()</code> method.
How can I resize the <code>mmap</code> object?


A:

The <code>resize()</code> method is on the <code>mmap</code> object, not the file object.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.tr
