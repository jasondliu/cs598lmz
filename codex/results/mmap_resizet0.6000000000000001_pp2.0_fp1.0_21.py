import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The code fails with:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
So how can I truncate a file and still use the mmap object?


A:

You can use the <code>mmap.resize()</code> method to resize the mapping:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
    m.close()
</code>
From the <code>mmap</code> documentation:
<blockquote>
<p><code>&lt;code&gt;mmap.resize(new_size)&lt;/code&gt;</code></p>
<p>Change the size of the mapped region. The new size can be larger or smaller than the previous size. If
