import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.write(bytes(1))
    print(a)
    m.flush()
</code>
The above code produces this output:
<code>b''
</code>
It seems like the <code>f.truncate()</code> step empties the os-level buffer that <code>mmap</code> wraps. But why is this buffer needed? Is there any way to flush it manually?


A:

Mark's reply explains why truncating the file affects the <code>mmap</code> object, and the documentation explains how to flush the object manually:
<blockquote>
<p>Under Unix, <code>&lt;code&gt;mmap&lt;/code&gt;</code>’s modifications to a file are not written back to the file until <code>&lt;code&gt;msync()&lt;/code&gt;</code> or <code>&lt;code&gt;munmap()&lt;/code&gt;</code> is called.</p>
</blockquote>
Perhaps surprisingly, Python <code>mmap</code>
