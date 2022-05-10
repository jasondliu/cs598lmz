import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
</code>
I am sure the file 'test' contains '1' before the execution, but the result is that 'test' contains '2'.
The question is why the file can be changed by mmap even if it is opened in read-only mode.


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>The <em>access</em> parameter determines whether changes made to the memory map are written back to the file on disk, and if so, whether those changes are visible to other processes mapping the same file, and if so, whether those changes are carried through to the underlying file even if the memory map is subsequently unmapped.</p>
</blockquote>
Since you didn't specify a value for <code>access</code>, it defaults to <code>ACCESS_DEFAULT</code> (which is 0). The documentation for <code>ACCESS_DEFAULT</code> says:
<blockquote>
<p>The default value is platform-dependent, but it is generally equal to <code>&lt;code&gt;
