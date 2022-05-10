import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This throws an exception on <code>a = m[:]</code>, but I'm unsure why.


A:

This is an expected behavior, according to the official documentation:
<blockquote>
<p>A <code>&lt;code&gt;ValueError&lt;/code&gt;</code> will be raised if the <code>&lt;code&gt;length&lt;/code&gt;</code> is greater than the current file size. <code>&lt;code&gt;mmap&lt;/code&gt;</code> cannot extend the file.</p>
</blockquote>
Ensure to provide a value greater than 0 to the <code>length</code> argument when opening the file.

