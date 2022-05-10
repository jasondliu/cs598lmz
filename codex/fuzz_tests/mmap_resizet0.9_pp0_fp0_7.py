import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I want to know the content of <code>a</code>, is it <code>bytes(1)</code> or <code>b''</code>.
The documentation of <code>mmap.mmap</code> says:
<blockquote>
<p>With mmap() operated in copy-on-write mode (prot == mmap.PROT_READ|mmap.PROT_WRITE and flags == MAP_PRIVATE), modifications to the mapped region will be write-protected and not visible to other processes mapping the same file, and will not be carried through to the underlying file. The modifications will become visible to other processes once the modified portion of the file is unmapped, or if msync() or mprotect() is called to un-write-protect the modified portion of the file.</p>
</blockquote>


A:

You can use <code>str</code> (Python 2) or <code>bytes</code> (Python 3) to examine the content of the memoryview <code>m</code>, e.g.:
<code>&gt;&gt;&gt; from mmap import *
