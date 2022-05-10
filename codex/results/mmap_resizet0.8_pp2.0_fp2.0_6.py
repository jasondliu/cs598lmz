import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
It crashes with:
<code>Segmentation fault: 11
</code>
If I change the file open mode to <code>r+b</code> I get a <code>ValueError</code> with the message <code>cannot mmap an empty file</code>.
How can I create a memory mapped file using Python 3.5?


A:

The documentation of the <code>mmap</code> module says:
<blockquote>
<p>It is an error to modify the file while it is mapped. Attempts to modify the file may raise a <code>&lt;code&gt;ValueError&lt;/code&gt;</code> exception. </p>
</blockquote>
http://docs.python.org/3/library/mmap.html#mmap.mmap
Therefore, your code is wrong. You need to either truncate the file or not mmap it.

