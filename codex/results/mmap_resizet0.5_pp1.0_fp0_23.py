import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect that <code>a</code> is <code>b'\x01'</code>, but it is <code>b''</code>.
How can I get <code>b'\x01'</code>?
This is a similar question to this, but the answer to the question is not my answer.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The file <em>must</em> be opened in <code>&lt;code&gt;mmap.ACCESS_READ&lt;/code&gt;</code> or <code>&lt;code&gt;mmap.ACCESS_WRITE&lt;/code&gt;</code> mode.</p>
</blockquote>
So you need to open the file in <code>mmap.ACCESS_READ</code> mode, and then you can use <code>mmap.mmap</code> to map the file:
<code>with open('test', 'r+b') as f:

