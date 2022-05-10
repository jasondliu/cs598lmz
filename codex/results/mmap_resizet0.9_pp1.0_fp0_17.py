import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises the following exception:
<code>ValueError: mmap offset is greater than file size
</code>
I can solve this problem by moving the line <code>f.truncate()</code> before <code>m = mmap.mmap(f.fileno(), 0)</code>. However, why is this? The documentation doesn't say anything about it when it comes to <code>mmap.mmap()</code>, except "If the file is larger than size, data beyond size is ignored."
This causes a problem for me because I'm using a library that accesses the contents of a file and truncates it.


A:

When you use <code>mmap</code> you're not accessing the file directly. Instead you're creating a <code>mmap</code> object that your process's memory manager uses just like any other control region (e.g., a stack, a heap, a shared library, etc.). The <code>mmap</code> object has a file descriptor, within your process, and so does the file itself. But they're not the same object, or even really related.
With a
