import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be <code>b'\x01'</code>, but it is <code>b''</code>. Is this a bug or am I missing something?


A:

As per the documentation:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> module defines the following exception:</p>
<p><strong><code>&lt;code&gt;OSError&lt;/code&gt;</code></strong></p>
<p>Raised when a function returns a system-related error, including I/O failures such as “file not found” or “disk full” (not for illegal argument types or other incidental errors).</p>
</blockquote>
Note that the error is raised from <code>f.truncate()</code>, not from <code>m[:]</code> as you might expect.

