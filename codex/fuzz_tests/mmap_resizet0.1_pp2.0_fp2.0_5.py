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
I understand that the mmap is pointing to the old file size, but I don't understand why it's not updated when I truncate the file.
I'm using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap object is not updated if the underlying file on disk is changed by another process. To update the mmap object, use the <code>&lt;code&gt;mmap.resize()&lt;/code&gt;</code> method.</p>
</blockquote>

