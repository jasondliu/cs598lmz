import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.close()
</code>
The last line raises <code>mmap.error: [Errno 22] Invalid argument</code>.
I'm using Python 3.5.2 on Ubuntu 16.04.


A:

From the docs:
<blockquote>
<p>The file must be opened in <code>&lt;code&gt;mmap.ACCESS_WRITE&lt;/code&gt;</code> mode.</p>
</blockquote>
So you need to open it in <code>r+b</code> mode:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.close()
</code>

