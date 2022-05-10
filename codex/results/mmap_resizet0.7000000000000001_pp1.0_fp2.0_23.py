import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
On my system the last statement raises a <code>ValueError</code> with the message
<blockquote>
<p>mmap: can't resize a read-only or copy-on-write file mapping object</p>
</blockquote>
The documentation of mmap.mmap doesn't say anything about a file having to be opened for writing for the mmap to be writable, so what is wrong with this code?


A:

Here is the relevant excerpt from the <code>mmap</code> docs, in the "Notes" section:
<blockquote>
<p>For the Unix implementation, mmap() is a wrapper around the system call of the same name. Note that this call may impose a limit on the size of the mapped region. On many systems, this limit is 128 MiB. The size argument to mmap() must be less than or equal to this limit.</p>
<p>Note also that <strong>the underlying file must be opened using the <code>&lt;code&gt;O_RDWR&lt;/code&gt;</code> or <code>&lt;code&
