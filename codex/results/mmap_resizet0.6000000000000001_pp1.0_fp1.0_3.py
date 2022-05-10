import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Here, I expect that <code>a</code> will be <code>b''</code>, but I get <code>b'\x01'</code>.
So, is <code>mmap.mmap</code> somehow caching the data? Or is it a bug in <code>mmap</code> module?


A:

It's a bug in the <code>mmap</code> module.
It's not caching the data, but it's not updating the internal size of the file.  It just keeps the old size, and so you get the old data back.
It's not a bug in the <code>mmap</code> module, it's doing what it's supposed to do.  <code>mmap</code> is a virtual memory mapping.  It has nothing to do with the size of the file.  It's just mapping to a certain size.  That size does not change when you truncate or grow the file.
It's not a bug in the <code>mmap</code> module.  It's doing what it's supposed to do.  It's mapping a certain size of memory
