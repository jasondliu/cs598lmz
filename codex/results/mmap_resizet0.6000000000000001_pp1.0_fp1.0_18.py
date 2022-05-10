import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(len(a))
</code>
This prints <code>0</code> instead of <code>1</code>.
Documentation is unclear about this. It says that mmap is "resized to match the size of the file", but a file is truncated, not resized.
Is this the expected behavior or a bug?


A:

Short answer: You should close the mmap object before truncating the file.

The mmap object is not "resized to match the size of the file", it is mapped to a region of the file. This region is not affected by changes to the file size.
From the documentation on <code>mmap.mmap()</code>
<blockquote>
<p><em>length</em> is ignored when <em>mmap</em> is used with <code>&lt;code&gt;ACCESS_COPY&lt;/code&gt;</code>.</p>
</blockquote>
<code>ACCESS_COPY</code> is used by default.
You can see that the mmap object is mapped to the beginning of the file
