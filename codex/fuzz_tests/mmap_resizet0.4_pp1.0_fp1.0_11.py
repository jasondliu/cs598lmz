import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected <code>a</code> to be <code>b'\x01'</code>, but instead it is <code>b''</code>.
If I change the <code>f.truncate()</code> line to <code>f.write(bytes(1))</code>, then <code>a</code> is <code>b'\x01'</code> as expected.
What is going on here?


A:

This is a known issue with the <code>mmap</code> module.
<blockquote>
<p>The mmap module defines the following exception:</p>
<p><code>&lt;code&gt;mmap.error&lt;/code&gt;</code></p>
<p>This exception is raised on any error.</p>
<p>The following functions are available:</p>
<p><code>&lt;code&gt;mmap.mmap(fileno, length[, tagname[, access[, offset]]])&lt;/code&gt;</code></p>
<p
