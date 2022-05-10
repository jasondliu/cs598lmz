import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m.resize(1024)
    print(m)
</code>
produces:
<code>&lt;mmap.mmap object at 0x7fdbdff7e6e0&gt;
mmap(1, 1024, prot_read|prot_write, map_shared, 3, 0)
</code>
The documentation for resize does not mention any way of getting meaningful values for prot_read and prot_write.
I would have expected to have some way of getting the numbers for
<code>mmap.PROT_READ
mmap.PROT_WRITE
</code>
may be from <code>m.prot</code> (or similar) which I cannot find.


A:

You could use the <code>mmap</code> module to directly get the desired values.
<blockquote>
<p>The mmap module defines the following constants:</p>
<pre><code>&lt;code&gt;PROT_READ   Pages may be read.
PROT_WRITE  Pages may be written.
PROT
