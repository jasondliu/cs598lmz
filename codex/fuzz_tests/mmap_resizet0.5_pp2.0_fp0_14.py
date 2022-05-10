import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
I suppose that this is because the memory map is not updated after truncating the file. Is there a way to do this?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The length argument specifies the initial size of the mapped region. This can not be larger than the file size.</p>
</blockquote>
So you can't make it larger than the file.
If you want to make it smaller, you need to use <code>mmap.resize</code>:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.res
