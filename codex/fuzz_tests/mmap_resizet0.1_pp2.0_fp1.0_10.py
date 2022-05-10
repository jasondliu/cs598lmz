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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the mmap is pointing to the old file, but I don't understand why it doesn't get updated when I truncate the file.
I'm using Python 3.6.1 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The optional <em>length</em> argument specifies the size of the mapped region. If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is omitted, the maximum length of the map is the current size of the file, except that if the file is empty Windows raises an exception (you cannot create an empty mapping on Windows).</p>
</blockquote>
So, you need to specify the
