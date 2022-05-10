import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
But if I change the <code>truncate</code> call to <code>f.truncate(1)</code>, the code works fine.
Why does this happen?


A:

The <code>mmap</code> object is not aware of the truncation, so it still thinks the file is 1 byte long.
From the <code>mmap</code> documentation:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function may need to extend the file size (beyond the <em>length</em> argument) in order to accommodate the whole mapping. If this causes the file to exceed its maximum length, <code>&lt;code&gt;mmap()&lt;/code&gt;</code> fails with <
