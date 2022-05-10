import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code should first create a file of size one. Then it opens the file, maps it and trucnates it. This fails with <code>OSError: [Errno 22] Invalid argument</code> on the <code>a = m[:]</code>.
Does this mean you cannot use an mmaped memory view (<code>m[:]</code>) after truncating the file like this?


A:

You can't use the mmaped fileview with the file-like object.
<blockquote>
<p><code>&lt;code&gt;mmap.nt fd[, length[, flags[, prot[, access[, offset]]]]]&lt;/code&gt;</code></p>
<p>Create a new memory-mapped file object.</p>
<p>...</p>
<p>If <em>fd</em> is not -1, it should return a file-like object that can be used with the mmap module to map an export of the file, and <em>os.fstat(fd)</em> can be used to get information about
