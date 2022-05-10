import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Gives me the following error for the last line:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I assume this is because the file is empty.
Is there a way to get the contents of a <code>mmap</code> object after truncating the file?


A:

According to the Python documentation:
<blockquote>
<p>mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])</p>
<p>...</p>
<p><em>offset</em> is the offset in the file where the mapping starts. Note that some systems require offset to be a multiple of the page size (e.g. 4096 on x86).</p>
</blockquote>
In this case, the offset is <code>0</code> since you are mapping the entire file.  The error is because the <code>offset</code> must be a multiple of the page size.

