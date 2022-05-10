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
I would expect that the mmap object would be updated to reflect the new file size.
Is there a way to do this without closing the file and reopening it?


A:

I think you need to call <code>m.resize()</code> after <code>f.truncate()</code> to update the mmap object.

