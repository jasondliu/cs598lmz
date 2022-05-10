import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I don't understand why. I have the impression that <code>f.truncate()</code> should resize the file to zero bytes, and <code>m</code> should be aware of this (because it is created from the file object).
I also tried to <code>m.resize(0)</code> before the <code>m[:]</code> call, but I get <code>ValueError: mmap can't resize a read-only or copy-on-write (COW) file</code>.
What I want to do is to resize the file to zero bytes, and then read the content of the file (which should be empty).
How can I do this?


A:

You can't.
The documentation states:
<blockquote>
<p>The mmap constructor creates a memory-mapped file. It is similar to the Unix system call <code>&lt;code&gt;mmap()&lt;/code&gt;</code>.</p>
</blockquote>

