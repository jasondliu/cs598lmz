import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm not entirely sure why it was failing, but I had a feeling it was the use of <code>mmap.mmap</code> with a file that had been truncated. But I can't find any documentation that states this is a problem.


A:

You can't use <code>mmap</code> with an empty file.  From the documentation:
<blockquote>
<p>New in version 3.3.</p>
<p>If length is 0, mmap() creates a new zero-length mapping, and the
  file descriptor is not actually mapped.</p>
</blockquote>

