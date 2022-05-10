import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I know you can use <code>mmap.resize</code> to get around this, but I don't want to resize the mmap. I just want it to be able to read the part of the file that it can.
Is that possible?


A:

<blockquote>
<p>I know you can use mmap.resize to get around this</p>
</blockquote>
No.  You cannot.  <code>mmap.resize</code> is not supported on Windows.  You would have to unmap and then map again, which is not what you want.
You might want to use <code>mmap.ACCESS_READ</code> instead of <code>mmap.ACCESS_WRITE</code>, but it is not clear from your example what you are trying to do.

