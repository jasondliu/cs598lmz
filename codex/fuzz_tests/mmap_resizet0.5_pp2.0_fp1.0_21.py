import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Is there a way to avoid this error?


A:

You can't.  The file has to be non-empty before you can use the <code>mmap</code> module.  The documentation says:
<blockquote>
<p>The length argument specifies the number of bytes to map. The entire file is mapped by default.</p>
</blockquote>
The <code>mmap</code> module is a wrapper around the <code>mmap</code> system call, which says:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function creates a new mapping in the virtual address space of the calling process. The starting address for the new mapping is specified in addr. The length argument specifies the length of the mapping.</p>
<p>The
