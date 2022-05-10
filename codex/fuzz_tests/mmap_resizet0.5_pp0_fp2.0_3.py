import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected that truncating the file would result in the underlying mmap object being invalidated, and so accessing it would raise an exception. Instead, the <code>a = m[:]</code> line succeeds and <code>a == b''</code>.
Is this the expected behavior? If so, why?


A:

<code>mmap</code> is a Python wrapper around the C <code>mmap</code> function, which is documented in the <code>mmap</code> man page.
The <code>mmap</code> man page says:
<blockquote>
<p>When a file is truncated, the effect on outstanding mappings of the portion of the file that was discarded depends on the implementation and mapping flags. In the following cases, the mapping is unaffected:</p>
<ul>
<li>The mapping was established using <code>&lt;code&gt;MAP_SHARED&lt;/code&gt;</code> and the file was opened with <code>&lt;code&gt;O_RDONLY&lt;/code&gt;</code>
