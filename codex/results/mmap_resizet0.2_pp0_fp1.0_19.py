import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I thought that the mmap object would be updated when the file is truncated.
I'm using Python 3.6.5 on Windows 10.


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is 0, the maximum length of the map is the current size of the file, except that if the file is empty <code>&lt;code&gt;mmap&lt;/code&gt;</code> fails.</p>
</blockquote>
So, when you truncate the file, the <code>mmap</code
