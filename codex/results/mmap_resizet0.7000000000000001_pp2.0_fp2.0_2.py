import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
This could be confusing, because we could think that <code>m</code> is a file-like object, and if we truncate the file, we would expect that the offset of <code>m</code> is updated.
I found that the following works:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    f.truncate()
    a = m[:]
</code>
But does this mean that once we have created a <code>mmap</code> object, we have no chance to truncate the file without raising an exception?
The <code>mmap</code> documentation says
<blockquote>
<p>If fileno specifies an invalid file descriptor, a <code>&
