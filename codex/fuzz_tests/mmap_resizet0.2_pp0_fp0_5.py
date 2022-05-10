import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure why this is happening. I'm using Python 3.5.2 on Windows 10.


A:

The <code>mmap</code> object is tied to the file size. When you truncate the file, the <code>mmap</code> object is no longer valid.
From the documentation:
<blockquote>
<p>mmap objects can be used anywhere a string is expected; for example, you can use the re module to search through a memory-mapped file. However, modifications to the file via a mmap object may not be immediately written to disk, and may not be visible to other programs accessing the same file. To force all modified data to be written to disk, use the flush() method. To force all modified data and metadata to be written to disk, use the sync() method.</p>
</blockquote>

