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
I would like to know why this happens and how to fix it.


A:

<code>mmap</code> is a view of the file.  When you truncate the file, the view is no longer valid.  You need to <code>close</code> the <code>mmap</code> object before truncating the file.

