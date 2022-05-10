import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would like to know if there is a way to truncate and then read the file.


A:

<code>mmap</code> is a view of a file.  If you truncate the file, the view is no longer valid.  You can't read from it.  You need to <code>close</code> the <code>mmap</code> object and then reopen it.

