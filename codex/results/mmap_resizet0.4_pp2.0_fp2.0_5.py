import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this case, I get the exception <code>OSError: [Errno 22] Invalid argument</code>.
I'm using Python 3.6.4 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> states:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is 0, the maximum length of the map is the current size of the file.</p>
</blockquote>
So, you can't use a length of 0.

