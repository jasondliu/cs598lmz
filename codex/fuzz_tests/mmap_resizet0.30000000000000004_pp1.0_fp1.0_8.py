import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect that the <code>m</code> object would be updated to reflect the new size of the file. Is this a bug in <code>mmap</code>?


A:

I think this is a bug in <code>mmap</code>.
<code>mmap</code> is a wrapper around the <code>mmap</code> system call, which is documented as follows:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function establishes a mapping between a process's address space and a file or shared memory object.  The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function is supported for regular files, the special file <code>&lt;code&gt;/
