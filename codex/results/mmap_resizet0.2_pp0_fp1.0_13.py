import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works as expected on Linux, but on Windows it raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Is there a way to make it work on Windows?


A:

The problem is that the <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function may need to update internal data structures after a file has been resized. To accommodate this, mmap() may need to unmap existing mappings before remapping the file. This means that any references to the data in the previous mapping are invalidated. To avoid this, you can use the <code>&lt;code&gt;MS_INVALIDATE&lt;/code&gt;</code> flag in the <code>&lt;code&gt;mmap()&lt;/code&gt;</code> call.</p>

