import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I expected the output to be <code>b'\x01'</code>.
Why is the output <code>b'\x00'</code>?
I'm using Python 3.6.5 on Windows 10.


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>If the file is resized by another process while it is open, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object can be safely used; it will reflect the new size.</p>
</blockquote>
So, you can't rely on the contents of the <code>mmap</code> object after the file has been truncated.

