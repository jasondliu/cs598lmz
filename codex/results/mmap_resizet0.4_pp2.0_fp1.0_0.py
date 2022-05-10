import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # mmap.error: [Errno 22] Invalid argument
</code>
I've tried to use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but it doesn't help.
Is there any way to fix this?


A:

You can't do this.
The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The mmap() function reserves a range of the process’s address space. The reserved range may overlap pages of any existing mapped file, anonymous mapping, or other reserved range of the process’s address space.</p>
</blockquote>
So, if you truncate the file, the memory map is no longer valid.

