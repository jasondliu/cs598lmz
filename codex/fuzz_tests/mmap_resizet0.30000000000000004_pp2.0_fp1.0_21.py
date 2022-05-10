import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Why is this happening? I thought that the mmap object would be updated when the file is truncated.


A:

The docs say:
<blockquote>
<p>The file size cannot be changed, but may be extended. To change the
  file size, use <code>&lt;code&gt;truncate()&lt;/code&gt;</code> before or after the <code>&lt;code&gt;mmap()&lt;/code&gt;</code> call.</p>
</blockquote>
So you need to call <code>truncate()</code> before the <code>mmap()</code> call.

