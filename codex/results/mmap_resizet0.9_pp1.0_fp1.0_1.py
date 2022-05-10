import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this case, the value of <code>a</code> is <code>b'\x00'</code>, but if I change <code>truncate()</code> to a direct call to <code>os.ftruncate()</code>, it will then be <code>b''</code>.
What is happening?
I am using CPython 3.4 and Linux.


A:

This is covered in the documentation for mmap:
<blockquote>
<p><code>&lt;code&gt;mmap.__new__(...)&lt;/code&gt;</code> method of builtins.type instance</p>
<p>...</p>
<p>In this case, <em>length</em> should reflect the current size of the file; the <em>mmap</em> object can be resized using the <em>resize()</em> method.</p>
<p>File objects that are opened in <code>&lt;code&gt;APPEND&lt;/code&gt;</code> mode, may only be memory
