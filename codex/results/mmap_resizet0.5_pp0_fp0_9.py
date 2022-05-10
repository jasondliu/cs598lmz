import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
This outputs <code>b'\x00'</code> instead of <code>b'\x01'</code>. I'm not sure why this is happening. I've tried changing the <code>mmap</code> mode to <code>r</code>, but that doesn't work either.


A:

The reason this is happening is that the <code>mmap</code> object is pointing to the old file, which has been truncated.
From the docs:
<blockquote>
<p>Note that modifications to the file while mmap’d are not guaranteed to be written through to disk.</p>
</blockquote>

