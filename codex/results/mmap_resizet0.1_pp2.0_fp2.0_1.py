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
I'm not sure why this is happening. I'm using Python 3.4.3.


A:

You are truncating the file after you created the mmap.
<code>m = mmap.mmap(f.fileno(), 0)
f.truncate()
</code>
The <code>mmap.mmap()</code> function takes the current file size as the second argument, and that is what you are using.
You can use <code>mmap.ALLOCATIONGRANULARITY</code> to get the system page size, or just use <code>mmap.PAGESIZE</code> (which is the same on Linux and OS X, but not on Windows).

