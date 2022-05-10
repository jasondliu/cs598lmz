import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Running this script produces the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Using mmap somehow retains the old size of the file even after <code>truncate()</code>, but I don't understand why.
If I change the line <code>f.truncate()</code> to <code>m.resize(0)</code>, the error disappears.
Can someone explain what's going on?
Note: this appears to be a Windows-only issue.


A:

I think it's because the <code>mmap</code> object caches the file size.  If you create the mmap object before truncating the file, it works:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.truncate(0)
    a = m[:]
</code>

