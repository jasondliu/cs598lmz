import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>MemoryError: invalid pointer</code>
The problem is that the size of the file is set to 0 bytes with <code>f.truncate()</code>. Does <code>mmap</code> hold the size of the file with the time of the <code>mmap</code> creation and don't update it with later calls to the <code>f.truncate()</code>? 


A:

Python's <code>mmap</code> uses <code>mmap(2)</code> system call under the covers. From documentation:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function establishes a mapping between a process’s virtual
  address space and a file, shared memory object, or <strong>Device</strong>. <code>&lt;code&gt;mmap()&lt;/code&gt;</code> creates
  a new mapping in the virtual address space of the calling process.
  The starting address for the new mapping is specified in <em>addr</em
