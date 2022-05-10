import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the variable a to be empty, but the content is still there. 
How can I achieve my goal?


A:

The size of a mmap() object is not affected by the underlying file size being changed. This is documented here: https://docs.python.org/3/library/mmap.html
<blockquote>
<p>Note that modifying a file via a mmap()‘d object may modify the
  underlying data on disk, so that data may be visible to other
  processes mapping the same file. This is true even when the mmap()‘d
  object is read-only.</p>
</blockquote>
You must call mmap.resize() to change the size of the mmap object.

