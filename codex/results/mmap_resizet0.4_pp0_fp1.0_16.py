import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Windows, but on Linux I get the following error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
The error is thrown when I try to get the slice of the <code>mmap</code> object.
I am using Python 3.6.1 on both platforms.
Is this a bug in Python or am I doing something wrong?


A:

<code>mmap.mmap</code> is not a file-like object. It is a memory-mapped file.
The documentation says:
<blockquote>
<p>The <code>&lt;code&gt;mmap&lt;/code&gt;</code> constructor creates a memory-map to an existing file. The file must remain open for the lifetime of the <code>&lt;code&gt;mmap&lt;/code&gt;</code>; you may not close it or truncate it until you are finished using the <code>&lt;code&gt;mmap&lt;/code&gt;</code>.</p>
</blockquote
