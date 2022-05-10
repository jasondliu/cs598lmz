import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I think that the problem is that the file is truncated before the mmap is updated.
Is there a way to update the mmap after the file is truncated?


A:

You can't use <code>mmap</code> on a file that has been truncated to zero length.
From the docs:
<blockquote>
<p>The mmap() function requires a file descriptor fd referring to an open file, and a length in bytes. The file descriptor must be opened with read permission, even if MAP_PRIVATE is specified.</p>
</blockquote>
The file descriptor is opened with read permission, but the file is empty, so there's nothing to read.

