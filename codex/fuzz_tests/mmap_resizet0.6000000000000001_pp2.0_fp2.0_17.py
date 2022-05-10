import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
This produces:
<code>b'\x00'
</code>
How does this work? How is it possible to read from a file after the file has been truncated?


A:

From the mmap documentation:
<blockquote>
<p>Python implements a <code>&lt;code&gt;mmap&lt;/code&gt;</code> module in the standard library as of Python 2.5. The <code>&lt;code&gt;mmap&lt;/code&gt;</code> module provides a nearly complete interface to the POSIX <code>&lt;code&gt;mmap&lt;/code&gt;</code> function.</p>
</blockquote>
The POSIX <code>mmap</code> function is specified as:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function establishes a mapping between a process's address space and a file, shared memory object, or typed memory object. The <code>&lt
