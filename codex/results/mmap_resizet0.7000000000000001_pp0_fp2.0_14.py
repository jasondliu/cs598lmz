import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Now, <code>a</code> is <code>''</code>, but I expected <code>'\x00'</code> because I truncated the file before taking view of the memory-mapped file.
So, my questions are:

Why does this happen?
When exactly does <code>mmap</code> get updated?



A:

<blockquote>
<p>When exactly does mmap get updated?</p>
</blockquote>
It's up to the kernel, but it's probably lazy, so you can be sure that it's not updated immediately after you truncate the file.
<blockquote>
<p>Why does this happen?</p>
</blockquote>
You're truncating the file before taking the view.

