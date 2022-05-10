import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm running on Windows 10, Python 3.6.5.
I've tried using <code>mmap.ACCESS_WRITE</code> and <code>mmap.ACCESS_COPY</code> instead of <code>mmap.ACCESS_READ</code>, but it didn't help.
I've also tried using <code>m.flush()</code> before <code>f.truncate()</code>, but it didn't help either.
Is there a way to truncate the file without getting this error?

