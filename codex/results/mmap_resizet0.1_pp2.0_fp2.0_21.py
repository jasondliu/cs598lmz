import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap(f.fileno(), 0)</code> to create the mmap. This creates a mmap of length 0, which is not what you want.
The documentation says:
<blockquote>
<p>If <em>length</em> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length of the map will be the current size of the file when <em>mmap</em> is called.</p>
</blockquote>
So, you should use <code>mmap.mmap(f.fil
