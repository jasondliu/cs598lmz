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
I would expect the mmap to be updated when the file is truncated.
Is there a way to do this?


A:

You can't do this.  The mmap is a view into the file, and the file is now smaller than the mmap.  You can't make the mmap smaller, so you have to close it and reopen it.

