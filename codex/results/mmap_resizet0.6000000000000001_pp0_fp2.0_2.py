import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
The reason is that the kernel and Python are working with different views of the file: the kernel knows the file is empty, but Python thinks it's full of <code>\x01</code>s.  So the <code>mmap</code> is invalid.
The kernel doesn't know that the file is empty until the <code>close()</code> happens.  If you avoid closing the file until after you've finished with the <code>mmap</code>, it will work fine.

