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
I don't understand why this is happening. I thought that the mmap would be updated when the file is truncated.
I'm using Python 3.6.5 on Windows 10.


A:

<blockquote>
<p>I thought that the mmap would be updated when the file is truncated.</p>
</blockquote>
That's not how it works.
The <code>mmap</code> object is a view of the file at a particular point in time.  If you change the file, the <code>mmap</code> object doesn't change.
If you want to change the file, you need to use the <code>mmap</code> object to do it.

