import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Why is this happening? I thought that the mmap object would be updated when the file is truncated.


A:

The mmap object is not updated when the file is truncated.
From the docs:
<blockquote>
<p>The mmap() function is supported on all Unix and Windows systems. On
  Unix, it is implemented using the mmap() system call. On Windows, it
  is implemented using the MapViewOfFile() function.</p>
</blockquote>
The mmap object is a view of the file, not the file itself.

