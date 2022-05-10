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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect that the mmap object would be updated to reflect the new file size.
Is there a way to do this without closing the file?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length of the map is the current size of the file when <em>mmap</em> is called.</p>
</blockquote>
So, you need to pass <code>0</code> as the length.

