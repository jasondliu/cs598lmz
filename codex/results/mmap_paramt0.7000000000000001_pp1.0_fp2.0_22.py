import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')
</code>
This code throws an <code>OSError: [Errno 22] Invalid argument</code>. I am running this on OS X.
I tried changing <code>mmap.mmap(f.fileno(), 0)</code> to <code>mmap.mmap(f.fileno(), 1)</code> and it worked.
But I want to be able to map the whole file.


A:

Actually, it is not possible to map a file in its entirety, as explained in the mmap documentation.
<blockquote>
<p>The <code>&lt;code&gt;length&lt;/code&gt;</code> argument specifies the number of bytes to map. The entire file may be used by specifying <code>&lt;code&gt;0&lt;/code&gt;</code> as the <code>&lt;code&gt;length&lt;/code&gt;</code> (this will only work on systems that support a <code>&lt;code&gt;size_t&lt;/
