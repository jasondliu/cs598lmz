import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    # m.close() # print(m.read(1)) is also not allowed

    # Cannot change size if opened for read.
    m.resize(100) # ValueError: resize on read-only endian handler
</code>
However, when mmap is opened with memoryview, it is possible to resize the mmap object.
I wonder why.


A:

<blockquote>
<pre><code>&lt;code&gt;m = mmap.mmap(f.fileno(), 0)
&lt;/code&gt;</code></pre>
</blockquote>
Sets the mmap size to 0 and thereafter can't be changed since it's mapped to the file of length 1.
<blockquote>
<pre><code>&lt;code&gt;m = memoryview(m)
&lt;/code&gt;</code></pre>
</blockquote>
Returns an object via which the mmap instance can be resized - since it's not mapped to a file.

