import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # TypeError: 'mmap.mmap' object does not support indexing
</code>
The output:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 11, in &lt;module&gt;
    a = m[:]
TypeError: 'mmap.mmap' object does not support indexing
</code>
Why? Is it not possible to index an mmap object?


A:

The error is right there in the manual:
<blockquote>
<p>The mmap constructor is used to create a memory-mapped file. It takes a file descriptor fd, the length of the mapping to create, optional flags and optional prot values. It returns an mmap object.</p>
</blockquote>
You can't use an mmap object like a string, you can only use it like a memory file.

